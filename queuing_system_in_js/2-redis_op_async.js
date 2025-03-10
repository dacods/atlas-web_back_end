import { createClient, print } from 'redis';
import { promisify } from 'util'

const client = createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

const getAsync = promisify(client.get).bind(client);

const setNewSchool = (schoolName, value) => {
    client.set(schoolName, value, print);
};

const displaySchoolValue = async (schoolName) => {
    try {
        const value = await getAsync(schoolName);
        console.log(value);
    } catch (err) {
        console.log(`Error getting value: ${err}`);
    }
};

(async () => {
    await displaySchoolValue('Holberton');
    setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
})();
    