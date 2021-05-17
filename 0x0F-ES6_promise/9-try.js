export default function guardrail(mathFunction) {
  const queue = [];

  try {
    const ret_value = mathFunction();

    queue.push(ret_value);
  } catch (e) {
    queue.push(e.toString());
  } finally {
    queue.push('Guardrail was processed');
  }

  return queue;
}
