const { readFile } = require('fs').promises;

async function getFile() {
   const file = await readFile('./app.js', 'utf-8');
}