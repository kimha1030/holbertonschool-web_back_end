export default function divideFunction(numerator, denominator) {
  if (denominator == 0) {
    throw Error('cannot divide by 0');
  }
  const op_divide = numerator / denominator;
  return op_divide;
}
