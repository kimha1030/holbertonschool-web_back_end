const assert = require('assert');
const calculateNumber = require('./0-calcul');

describe('test_calculateNumber', () => {
  it('sum with different number of arguments', () => {
    assert.equal(isNaN(calculateNumber()), true);
    assert.equal(isNaN(calculateNumber(4)), true);
    assert.equal(calculateNumber(1, 2, 3), 3);
  });
  it('sum two integers', () => {
    assert.equal(calculateNumber(1, 3), 4);
  });
  it('sum of integer and float rounded above', () => {
    assert.equal(calculateNumber(1, 3.7), 5);
  });
  it('sum of float rounded below and integer', () => {
    assert.equal(calculateNumber(2.3, 4), 6);
  });
  it('sum two floats', () => {
    assert.equal(calculateNumber(1.2, 3.7), 5);
  });
  it('sum with zero', () => {
    assert.equal(calculateNumber(1.6, 0), 2);
    assert.equal(calculateNumber(0.3, 0), 0);
  });
  it('sum two negative numbers', () => {
    assert.equal(calculateNumber(-1.9, -7.7), -10);
  });
});
