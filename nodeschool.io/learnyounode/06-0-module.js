const fs = require('fs');
const path = require('path');

module.exports = function(dir, ext, callback) {
  fs.readdir(dir, function(err, data) {
    if (err) {
      return callback(err);
    }
    else {
      callback(null, data.filter(f => path.extname(f) === '.' + ext));
    }
  });
}
