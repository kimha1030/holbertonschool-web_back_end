export default function cleanSet(set, startString) {
  const valStr = "";
  if (startString == "") {
    return valStr;
    for (const i of set) {
      if (i.startsWith(startString)) {
        const lenStart = startString.length;
        valStr = valStr + `${i.slice(lenStart)}-`;
      }
    }
    const lenStr = valStr.length;
    return valStr.slice(0, lenStr - 1);
  }
}
