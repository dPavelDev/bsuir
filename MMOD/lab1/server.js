const app = require('express')();
const http = require('http').Server(app);
const io = require('socket.io')(http);

const pearsonCorrelation = require('./pearson');

const mulMethod = (c, m, a0, k) => {
  let a = [a0];
  let ai = a0;

  for(let i = 1; i < k; i++) {
    a[i] = c * ai % m;
    ai = a[i];
  }

  a = a.map((ai) => {return ai/m});

  return a;
};

const halfSquareMethod = (n, k) => {
  let z = [];

  for(let i = 0; i < k; i++) {
    n *= n;
    n = '' + n;

    while(n.length !== 8) {
      n = '0' + n;
    }
    n = parseInt(n.slice(2,6));

    z[i] = n;
  }

  z = z.map((zi) => {return zi / 9999});

  return z;
};

const testUniform = (z, k) => {
  let n = Array.from({ length: k }, () => 0);

  let i = 1;
  for(let zi of z.sort()){
    if(zi > i/k) i++;
    n[i-1]++;
  }

  return n.map(ni => ni / z.length);
};

function getAvg(grades) {
  return grades.reduce(function (p, c) {
      return p + c;
    }) / grades.length;
}

if(module.parent) {
  exports.mulMethod = mulMethod;
} else {
  app.get('/', function (req, res) {
    res.sendFile(__dirname + '/index.html');
  });

  io.on('connection', function (socket) {
    let m = 12345,
      c = 7777,
      n = 9421,
      k1 = 100,
      k2 = 10000;

    let z = halfSquareMethod(n, k1);
    io.emit('halfSquareMethod', testUniform(z, 10));

    z = halfSquareMethod(n, k2);
    io.emit('halfSquareMethod10k', testUniform(z, 10));

    z = mulMethod(c, m, 1, k1);
    io.emit('mulMethod', testUniform(z, 10));

    z = mulMethod(c, m, 1, k2*10);
    io.emit('mulMethod10k', testUniform(z, 10));
    M = getAvg(z);
    D = z.reduce((sum, value) => sum + (value - M) * (value - M), 0) / z.length;

    console.log('Мат ожидание:', M);
    console.log('Дисперсия:', D);
    console.log('----------------------');
  });

  http.listen(3000, function () {
    console.log('listening on : 3000');
  });
}