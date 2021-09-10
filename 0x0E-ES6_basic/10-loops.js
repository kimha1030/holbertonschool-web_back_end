export default function appendToEachArrayValue(array, appendString) {
  const avalues = [];
  for (const value of array) {
    avalues.push(appendString + value);
  }

  return avalues;
}
