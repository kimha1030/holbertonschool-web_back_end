export default function guardrail(mathFunction) {
  const queue = [];
  try {
    const retvalue = mathFunction();
    queue.push(retvalue);
  } catch (e) {
    queue.push(e.toString());
  } finally {
    queue.push('Guardrail was processed');
  }
  return queue;
}
