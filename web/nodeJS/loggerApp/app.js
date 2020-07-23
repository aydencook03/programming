const Logger = require('./Logger.js');
const logger = new Logger();

// Register a Listener
logger.addListener('messageLogged', function(arg) {
    console.log('Listener Called With', arg);
});

logger.log('Hello');
