const os = require('os');

var totalMem = os.totalmem();
var freeMem = os.freemem();

console.log(`Total Memory: ${totalMem} \nFree Memory: ${freeMem}`);
