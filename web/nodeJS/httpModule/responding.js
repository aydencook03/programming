http = require('http');

const server = http.createServer(function(req, res) {
    if (req.url === '/') {
        res.write('Hello World');
        res.end();
    }
    if (req.url === '/numbers') {
        res.write(JSON.stringify([0, 1, 2, 3, 4, 5]));
        res.end();
    }
});

const port = 3000;

server.on('connection', function(socket) {
    console.log('New Connection...');
});

server.listen(port); // server raises an event on new connection to port

console.log(`Listening on Port ${port}...`);

// server is an instance of https.Server, which inherits from net.Server, which is an extended event.EventEmitter
//server.addListener() or server.on();
//server.listen(port) ->>> server.emit() when there is a new connection on port;
