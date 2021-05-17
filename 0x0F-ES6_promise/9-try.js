export default function guardrail(mathFunction) {
  const queue = [];
  try {
    let retValue = mathFunction();
    queue.push(retValue);
  } catch (e) {
    queue.push(e.toString());
  } finally {
    queue.push('Guardrail was processed');
  }
  return queue;
}
