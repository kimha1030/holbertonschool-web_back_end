const assert = require('assert');
const calculateNumber = require('./1-calcul');

describe('test_sum_calculateNumber', () => {
  it('sum with different number of arguments', () => {
    assert.equal(isNaN(calculateNumber()), true);
    assert.equal(isNaN(calculateNumber('SUM', 4)), true);
    assert.equal(calculateNumber('SUM', 1, 2, 3), 3);
  });
  it('sum two integers', () => {
    assert.equal(calculateNumber('SUM', 1, 3), 4);
  });
  it('sum of integer and float rounded above', () => {
    assert.equal(calculateNumber('SUM', 1, 3.7), 5);
  });
  it('sum of float rounded below and integer', () => {
    assert.equal(calculateNumber('SUM', 2.3, 4), 6);
  });
  it('sum two floats', () => {
    assert.equal(calculateNumber('SUM', 1.2, 3.7), 5);
  });
  it('sum with zero', () => {
    assert.equal(calculateNumber('SUM', 1.6, 0), 2);
    assert.equal(calculateNumber('SUM', 0.3, 0), 0);
  });
  it('sum two negative numbers', () => {
    assert.equal(calculateNumber('SUM', -1.9, -7.7), -10);
  });
});

describe('test_substract_calculateNumber', () => {
  it('substract with different number of arguments', () => {
    assert.equal(isNaN(calculateNumber()), true);
    assert.equal(isNaN(calculateNumber('SUBTRACT', 4)), true);
    assert.equal(calculateNumber('SUBTRACT', 4, 2, 3), 2);
  });
  it('substract two integers', () => {
    assert.equal(calculateNumber('SUBTRACT', 5, 3), 2);
  });
  it('substract of integer and float rounded above', () => {
    assert.equal(calculateNumber('SUBTRACT', 4, 3.7), 0);
  });
  it('substract of float rounded below and integer', () => {
    assert.equal(calculateNumber('SUBTRACT', 5.3, 2), 3);
  });
  it('substract two floats', () => {
    assert.equal(calculateNumber('SUBTRACT', 6.2, 4.4), 2);
  });
  it('substract with zero', () => {
    assert.equal(calculateNumber('SUBTRACT', 3, 0), 3);
    assert.equal(calculateNumber('SUBTRACT', 0.2, 0), 0);
  });
  it('substract two negative numbers', () => {
    assert.equal(calculateNumber('SUBTRACT', -3.9, -1.2), -3);
  });
});

describe('test_divide_calculateNumber', () => {
  it('divide with different number of arguments', () => {
    assert.equal(isNaN(calculateNumber()), true);
    assert.equal(isNaN(calculateNumber('DIVIDE', 4)), true);
    assert.equal(calculateNumber('DIVIDE', 1.8, 2, 5), 1);
  });
  it('divide two integers', () => {
    assert.equal(calculateNumber('DIVIDE', 6, 3), 2);
  });
  it('divide of integer and float rounded above', () => {
    assert.equal(calculateNumber('DIVIDE', 9, 2.7), 3);
  });
  it('divide of float rounded below and integer', () => {
    assert.equal(calculateNumber('DIVIDE', 8.3, 4), 2);
  });
  it('divide two floats', () => {
    assert.equal(calculateNumber('DIVIDE', 5.7, 2.8), 2);
  });
  it('divide with zero', () => {
    assert.equal(calculateNumber('DIVIDE', 1.6, 0), 'Error');
    assert.equal(calculateNumber('DIVIDE', 0, 8), 0);
  });
  it('divide two negative numbers', () => {
    assert.equal(calculateNumber('DIVIDE', -7.9, -3.7), 2);
  });
});

describe('test_type_calculateNumber', () => {
  it('if type of first argument is different of SUM, SUBSTRACT, DIVIDE', () => {
    assert.ifError(calculateNumber('POW', 2, 3), 'UNDEFINED');
  });
});
