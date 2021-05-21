export default function updateStudentGradeByCity(arrayObjs, city, newGrades) {
  const filterStudents = arrayObjs.filter((i) => i.location === city);
  return filterStudents.map((i) => {
    const newGrade = newGrades.filter((j) => j.studentId === i.id);
    let grade;
    if (newGrade[0]) {
      grade = newGrade[0].grade;
    } else {
      grade = 'N/A';
    }
    return {
      ...i,
      grade
    };
  });
}

