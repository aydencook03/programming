const EventEmitter = require('events'); // returns a class

let url = 'https://loggerurl.io/log';

class Logger extends EventEmitter {
    log(message) {
        console.log(message);
    
        // Raise an event
         this.emit('messageLogged', {id: 0, message: message}); // raises event 'messageLogged' with arguments    
    }   
}

module.exports = Logger;
