import { createClient } from 'redis';

const client = createClient();

client.on('connect', () => {
    console.log('Redis client connected to the server');
});
client.on('error', (err) => {
    console.log('Redis client not connected to the server:', err);
});

client.on('message', (message, channel) => {
    if (channel == 'holberton school channel') {
        console.log(message);
    }
    if (message == 'KILL_SERVER') {
        client.unsubscribe('holberton school channel');
        client.quit();
    }
});
client.subscribe('holberton school channel');
