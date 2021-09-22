export default function updateUniqueItems(map) {
  if (map instanceof Map) {
    for (const [k, v] of map.entries()) {
      if (v === 1) {
        map.set(k, 100);
      }
    }
  } else {
    throw Error('Cannot process');
  }
  return map;
}
