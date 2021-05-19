export default function getListStudentIds(arrayObjs) {
  if (Array.isArray(arrayObjs) === false) {
    return [];
  }
  return arrayObjs.map((i) => i.id);
}
