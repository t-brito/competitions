var fs = require('fs');

let str = fs.readFileSync(process.argv[2], 'utf8');

// let buf = fs.readFileSync(process.argv[2]);
// let str = buf.toString();

let arr = str.split('\n');

let noLines = arr.length - 1;

console.log(noLines);
