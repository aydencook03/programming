const EventEmitter = require('events');
const emitter = new EventEmitter();

// Register Listener
emitter.addListener('messageLogged', function(arg) {
    console.log('Listener Called With', arg);
})

// Raise Event
emitter.emit('messageLogged', {id: 0, arg: 'test'})
