const http = require('http');

http.get(process.argv[2], function (resp) {
  resp.setEncoding('utf8');
  resp.on('data', (data) => console.log(data));
  resp.on('error', (error) => console.error(error));
  resp.on('end', (end) => console.log(''));
});
