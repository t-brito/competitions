const net = require('net');
const strftime = require('strftime');

function listener(socket) {
  data = strftime('%Y-%m-%d %H:%M\n', new Date());
  // socket.write(data);
  // socket.end() also takes data object - use instead of .write()
  socket.end(data);
}

var server = net.createServer(listener);

server.listen(Number(process.argv[2]));
