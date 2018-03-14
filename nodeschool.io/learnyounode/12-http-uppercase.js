const map = require('through2-map');
const http = require('http');

const portNumber = Number(process.argv[2]);

let server = http.createServer(function(req, res) {
  if (req.method !== 'POST') {
    return res.end('send me a POST\n');
  }
  req.pipe(map(function(chunk) {
    return chunk.toString().toUpperCase();
  })).pipe(res);
});

server.listen(portNumber);
