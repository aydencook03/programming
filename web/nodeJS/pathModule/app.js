const path = require('path');

var pathObj = path.parse(__filename); // __filename is a part of the module function wrapper ie. built in to each module

console.log(__filename + '\n' +  __dirname);
console.log(pathObj);
