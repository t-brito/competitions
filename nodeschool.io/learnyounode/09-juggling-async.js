const http = require('http');
const bl = require('bl');

var urls = [process.argv[2], process.argv[3], process.argv[4]];

var count = 3;
var strings = [];

function printResults() {
  for (let i = 0; i < 3; ++i) {
    console.log(strings[i]);
  }
}

urls.forEach(function (url, index) {
  http.get(url, function(resp) {
    resp.pipe(bl(function(err, data) {
      if (err) {
        return console.error(err);
      }
      strings[index] = data.toString();
      --count;
      if  (count === 0) {
        printResults();
      }
    }));
  });
});
