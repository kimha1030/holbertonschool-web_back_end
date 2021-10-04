const express = require('express');
const countStudents = require('./3-read_file_async');

const pathCSV = process.argv.slice(2)[0];

const app = express();
app.get('/', (request, response) => response.send('Hello Holberton School!'));
app.get('/students', async (request, response) => {
  const txt = 'This is the list of our students\n';
  try {
    const info = await countStudents(pathCSV);
    // console.log(info);
    response.send(`${txt}${info.join('\n')}`);
  } catch (e) {
    response.send(`${txt}${e.message}`);
  }
});
app.listen(1245);
module.exports = app;
