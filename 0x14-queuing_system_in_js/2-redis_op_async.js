import redis from 'redis';
import { createClient } from 'redis';
import { promisify } from 'util';

const client = createClient();
const prom = promisify(client.get).bind(client);
client.on('connect', () => {
    console.log('Redis client connected to the server')
});
client.on('error', (err) => {
    console.log('Redis client not connected to the server:', err)
});

function setNewSchool(schoolName, value) {
    client.set(schoolName, value, redis.print)
}

async function displaySchoolValue(schoolName) {
    const res = await prom(schoolName);
    console.log(res);
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
