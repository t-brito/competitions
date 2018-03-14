const fs = require('fs');
const path = require('path');

var dir = process.argv[2];
var ext = '.' + process.argv[3];

fs.readdir(dir, function(err, files) {
  if (err) {
    console.error(err);
  }
  else {
    files.forEach((f) => {
      if (path.extname(f) === ext) {
        console.log(f);
      }
    })
  }
});
