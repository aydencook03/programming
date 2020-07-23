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
