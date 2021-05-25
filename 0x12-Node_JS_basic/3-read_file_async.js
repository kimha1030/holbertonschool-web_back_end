const fs = require('fs');

function countStudents(pathArg) {
  return new Promise((resolve, reject) => {
    fs.readFile(pathArg, 'utf-8', (e, data) => {
      if (e) {
        reject(Error('Cannot load the database'));
      }
      if (data) {
        const strLine = data.toString().split('\n');
        const studList = {};
        for (let i = 1; i < strLine.length - 1; i += 1) {
          const word = strLine[i].split(',');
          if (studList[word[3]]) {
            studList[word[3]].numStudents += 1;
            studList[word[3]].nameStudents.push(` ${word[0]}`);
          } else {
            studList[word[3]] = { numStudents: 1, nameStudents: [`${word[0]}`] };
          }
        }
        const totalStudents = strLine.length - 2; // Menos encabezado y ultima fila
        console.log(`Number of students: ${totalStudents}`);
        for (const s in studList) {
          if (Object.prototype.hasOwnProperty.call(studList, s)) {
            console.log(
              `Number of students in ${s}: ${studList[s].numStudents}. List: ${studList[s].nameStudents}`,
            );
          }
        }
      }
      resolve();
    });
  });
}

module.exports = countStudents;
