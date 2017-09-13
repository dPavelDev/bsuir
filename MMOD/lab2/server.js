const app = require('express')();
const http = require('http').Server(app);
const io = require('socket.io')(http);
const rv = require('../lab1/server.js');

app.get('/', function(req, res){
  res.sendFile(__dirname + '/index.html');
});

const randomEvent = (p, x) => {
  return x.reduce((res, value) => {
    res[value <= p ? 0 : 1]++;
    return res;
  }, [0, 0]).map(item => item / x.length);
};

const complexEvent = (pA, x1, pB, x2, pBA) => {
  let ans = [0,0,0,0];

  const notAB = 1 - ((pA - pBA * pB)/(1 - pB));

  for(let i = 0, x1Item, x2Item; i < x1.length; i++) {
    x1Item = x1[i];
    x2Item = x2[i];

    if (x1Item <= pA) {
      // AB || A*B*
      if (x2Item <= pBA) {
        ans[0]++; // AB
      } else {
        ans[2]++; // A*B*
      }
    } else {
      // AB* || A*B
      if (x2Item <= notAB) {
        ans[1]++; //A*B
      } else {
        ans[3]++; // AB*
      }
    }
  }

  return ans.map(item => item / x1.length);
};

const fullEvent = (p, x) => {
  let ans = new Array(6).fill(0);

  for(let i = 0; i < x.length; i++) {
    for(let j = 0; j < p.length - 1; j++) {
      if (x[i] >= p[j] && x[i] < p[j+1]) {
        ans[j]++;
      }
    }
  }

  return ans.map(a => a / x.length);
};

io.on('connection', function(socket){

  let p = 0.6;
  let x = rv.mulMethod(44555, 12345, 1, 10000);

  io.emit('randomEvent1', randomEvent(p, x));

  let pa = 0.4,
    pb = 0.5,
    pba = 0.6,
    pb_a = (pb - pba * pa)/(1 - pa),
    x1 = rv.mulMethod(44555, 12345, 1, 10000),
    x2 = rv.mulMethod(33444, 54321, 1, 10000);

  io.emit('randomEvent2', complexEvent(pa, x1, pba, x2, pb_a));

  p = [0, 0.15, 0.3, 0.45, 0.6, 0.75, 0.9];
  x = rv.mulMethod(44555, 12345, 1, 10000);

  io.emit('randomEvent3', fullEvent(p, x));
});

http.listen(9000, function(){
  console.log('listening on :9000');
});
