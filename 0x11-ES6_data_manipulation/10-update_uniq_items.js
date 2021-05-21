export default function updateUniqueItems(map) {
  if (map instanceof Map) {
    for (const k of map) {
      if (map.get(k) === 1) {
        map.set(k, 100);
      }
    }
  } else {
    throw Error('Cannot process');
  }
  return map;
}
