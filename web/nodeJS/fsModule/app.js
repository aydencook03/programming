const fs = require('fs');


const files = fs.readdirSync('./'); //syncronous
console.log(files);
const filesAsync = fs.readdir('./', logFiles); //asyncronous, calls logFiles() when finished

function logFiles(error, files) {
	if(error) {
		console.log('Error ', error);
	} else {
		console.log(files);
	}
}

/////////////////////////////////////////
const {readFile, readFileSync} = require('fs');

const txtSync = readFileSync('./app.js', 'utf-8');
//console.log(txtSync);

const txt = readFile('./app.js', 'utf-8', (err, txt) => {
	if(err) {
		console.log('error:', err);
	} else {
		console.log(txt);
	}
});

console.log('do this ASAP'); // this is ran before 'const txt' because of asynchronosity