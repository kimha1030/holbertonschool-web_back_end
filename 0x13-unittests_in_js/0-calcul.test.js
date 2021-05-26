const assert = require('assert').strict;
const calculateNumber = require('./0-calcul.js');

describe('test calculateNumber', () => {
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
  });
  it('sum with a single argument', () => {
    assert.equal(isNaN(calculateNumber(4)), true);
  });
});
