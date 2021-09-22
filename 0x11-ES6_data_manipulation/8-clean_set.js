export default function cleanSet(set, startString) {
  let valStr = '';
  if (startString === '') {
    return valStr;
  }
  set.forEach((i) => {
    if (i.includes(startString)) {
      valStr = valStr.concat(`-${i.replace(startString, '')}`);
    }
  });
  valStr = valStr.substring(1);

  return valStr;
}
