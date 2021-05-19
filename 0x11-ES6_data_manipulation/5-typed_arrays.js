export default function createInt8TypedArray(length, position, value) {
  const buffer = new ArrayBuffer(length);
  const view = new Uint8Array(buffer);
  const dataView = new DataView(buffer, 0);
  const lenArray = length - 1;
  if (position > lenArray) {
    throw Error('Position outside range');
  }
  return dataView;
}
