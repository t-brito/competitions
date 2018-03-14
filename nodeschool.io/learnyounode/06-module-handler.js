var mod = require('./06-0-module.js');

var dir = process.argv[2];
var ext = process.argv[3];

var callback = function (err, data) {
  if (err) {
    return console.error(err);
  }
  else {
    data.forEach(f => console.log(f))
  }
};

mod(dir,ext, callback);
