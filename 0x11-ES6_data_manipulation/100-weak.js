export const weakMap = new WeakMap();

export function queryAPI(endpoint) {
  const num = weakMap.get(endpoint);
  if (num) {
    weakMap.set(endpoint, num + 1);
  } else {
    weakMap.set(endpoint, 1);
  }
  if (num >= 5) {
    throw Error('Endpoint load is high');
  }
}
