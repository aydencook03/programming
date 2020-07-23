http = require('http');

const server = http.createServer();

const port = 3000;

server.on('connection', (socket) => { // function(socket)
    console.log('New Connection...');
})

server.listen(port); // server raises an event on new connection to port

console.log(`[Listening on Port] ${port}`);

// server is an instance of https.Server, which inherits from net.Server, which is an extended event.EventEmitter
//server.addListener();
//server.emit();
