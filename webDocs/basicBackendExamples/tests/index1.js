// behind the scenes of the game
var express = require('express'); // needs this library
var app = express();
var port = process.env.PORT || 3000;  // what port to open it on must have the option to be
// chosen by server if you want it to be heroku compatible, also does need the default
var server = require('http').createServer(app).listen(port);
var socket = require('socket.io');
var io = socket(server);
app.use(express.static('public'));

var request = require('request');

request.post('index.html', { form: { fname: 'value' } } );

console.log("server running");

io.sockets.on('connection', newConnection);  // when you get a connection do this

function newConnection(socket) {
  console.log("new connection");

  socket.on('disconnect', handleDisconnect);
  function handleDisconnect(data) {
    console.log("disconnect")
  }

}


