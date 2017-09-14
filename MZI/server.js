const app = require('express')();
const http = require('http').Server(app);
const io = require('socket.io')(http);

const CaesarShift = require('./lab1');
const AES = require('./lab3');

app.get('/', function(req, res){
  res.sendFile(__dirname + '/index.html');
});

AES.init();

io.on('connection', function(socket){
  // LAB1 --- CAESAR -------
  socket.on('caesarEncrypt', function(data){
    const { text, shift } = JSON.parse(data);
    socket.emit('caesarResult', CaesarShift(text, parseInt(shift, 10)));
  });

  socket.on('caesarDecrypt', function(data){
    const { text, shift } = JSON.parse(data);
    socket.emit('caesarResult', CaesarShift(text, -1 * parseInt(shift, 10)));
  });
  // -------------------------


  // LAB3 ------- AES ---------
  socket.on('aesEncrypt', function(data){
    let { text, key } = JSON.parse(data);

    text = text.split('').map(char => char.charCodeAt(0));
    key = key.split('').map(char => char.charCodeAt(0));

    if (key.length < 32) {
      for(let i = key.length; i < 32; i++) key.push(0);
    } else if (key.length < 64) {
      for(let i = key.length; i < 64; i++) key.push(0);
    } else if (key.length < 128) {
      for(let i = key.length; i < 128; i++) key.push(0);
    }

    AES.expandKey(key);
    AES.encrypt(text, key);

    socket.emit('aesResult', text);
  });

  socket.on('aesDecrypt', function(data){
    let { text, key } = JSON.parse(data);

    text = text.split(',');
    key = key.split('').map(char => char.charCodeAt(0));

    if (key.length < 32) {
      for(let i = key.length; i < 32; i++) key.push(0);
    } else if (key.length < 64) {
      for(let i = key.length; i < 64; i++) key.push(0);
    } else if (key.length < 128) {
      for(let i = key.length; i < 128; i++) key.push(0);
    }

    AES.expandKey(key);
    AES.decrypt(text, key);
    text = text.map(char => String.fromCharCode(char)).join('');

    socket.emit('aesResult', text);
  });
  // ----------------------------
});

http.listen(3000, function(){
  console.log('listening on *:3000');
});