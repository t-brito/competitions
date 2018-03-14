const http = require('http');
const url = require('url');

const portNumber = Number(process.argv[2]);

const path_parse = '/api/parsetime';
const path_unix = '/api/unixtime';

let server = http.createServer(function(req, res) {
  if (req.method !== 'GET') {
    return res.end('send me a GET\n');
  }

  let url_data = url.parse(req.url, true);

  let date = new Date(url_data.query.iso);
  let data;

  if (url_data.pathname === path_parse) {
    data = {
      hour: date.getHours(),
      minute: date.getMinutes(),
      second: date.getSeconds()
    };
  }

  else if (url_data.pathname === path_unix) {
    data = {
      unixtime: date.getTime()
    };
  }

  if (!data) {
    res.writeHead(404);
    res.end();
  }
  else {
    res.writeHead(200, { 'Content-Type': 'application/json' });
    res.end(JSON.stringify(data), null, 2);
  }
});
server.listen(portNumber);
