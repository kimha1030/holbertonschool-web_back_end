export default function appendToEachArrayValue (array, appendString) {
  const arrayValues = [];
  for (const value of array) {
    arrayValues.push(appendString + value);
  }

  return array;
}
