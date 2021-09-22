export default function cleanSet(set, startString) {
  let valStr = '';
  if (startString === '') {
    return valStr;
  }
  set.forEach((i) => {
    if (i && i.startsWith(startString)) {
      let sum = '';
      if (valStr.length === 0) {
        sum = i.replace(startString, '');
      } else {
        sum = i.replace(startString, '-');
      }
      valStr += sum;
    }
  });
  return valStr;
}
