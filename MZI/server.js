var app = require('express')();
var http = require('http').Server(app);
var io = require('socket.io')(http);

const CaesarShift = require('./lab1');

app.get('/', function(req, res){
  res.sendFile(__dirname + '/index.html');
});

io.on('connection', function(socket){
  socket.on('caesarEncrypt', function(data){
    const { text, shift } = JSON.parse(data);
    socket.emit('caesarResult', CaesarShift(text, parseInt(shift, 10)));
  });

  socket.on('caesarDecrypt', function(data){
    const { text, shift } = JSON.parse(data);
    socket.emit('caesarResult', CaesarShift(text, -1 * parseInt(shift, 10)));
  });
});

http.listen(3000, function(){
  console.log('listening on *:3000');
});