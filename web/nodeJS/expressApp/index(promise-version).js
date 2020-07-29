const { readFile } = require('fs').promises;
const express = require('express');

const app = express();

app.get('/', async (request, response) => {
    response.send(await readFile('./brickbreaker.html', 'utf-8'));
    console.log('Connection');
});

app.listen(3000, () => {console.log('App available at http://localhost:3000')});