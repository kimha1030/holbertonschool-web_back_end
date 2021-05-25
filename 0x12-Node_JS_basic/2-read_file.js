const fs = require('fs');

function countStudents(pathArg) {
  try {
    const info = fs.readFileSync(pathArg, 'utf-8');
    const strLine = info.toString().split('\n');
    const studList = {};
    for (let i = 1; i < strLine.length - 1; i++) {
      const word = strLine[i].split(',');
      if (studList[word[3]]) {
        studList[word[3]].numStudents = studList[word[3]].numStudents + 1;
        studList[word[3]].nameStudents.push(` ${word[0]}`);
      } else {
        studList[word[3]] = { numStudents: 1, nameStudents: [`${word[0]}`] };
      }
    }
    const totalStudents = strLine.length - 2; // Menos encabezado y ultima fila
    console.log(`Number of students: ${totalStudents}`);
    for (const s in studList) {
      console.log(
        `Number of students in ${s}: ${studList[s].numStudents}. List: ${studList[s].nameStudents}`,
      );
    }
  } catch (e) {
    throw new Error('Cannot load the database');
  }
}

module.exports = countStudents;
