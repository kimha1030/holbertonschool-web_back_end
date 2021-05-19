export default function hasValuesFromArray(set, array) {
  const elemsExist = array.every((i) => set.has(i));
  return elemsExist;
}
