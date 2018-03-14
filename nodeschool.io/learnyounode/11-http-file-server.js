const fs = require('fs');
const http = require('http');

let portNumber = +process.argv[2];
let file = process.argv[3];

let server = http.createServer(function(req, res) {
  // did not put this in my original solution
  res.writeHead(200, { 'content-type': 'text/plain' })

  let src = fs.createReadStream(file);
  src.pipe(res);
});

server.listen(portNumber);
