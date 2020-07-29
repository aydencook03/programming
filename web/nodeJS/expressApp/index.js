const express = require('express');
const {readFile} = require('fs');

const app = express();

app.get('/', (request, response) => {
    readFile('./brickbreaker.html', 'utf-8', (err, data) => {
        if(err) {
            response.status(500);
        } else {
            response.send(data);
        }
    });
    console.log('Connection Received');
});

app.listen(3000, () => {console.log('App Available on http://localhost:3000')});