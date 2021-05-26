const { expect } = require('chai');
const calculateNumber = require('./1-calcul');

describe('test_chai_sum_calculateNumber', () => {
  it('sum with different number of arguments', () => {
    expect(calculateNumber()).to.equal(undefined);
    expect(calculateNumber('SUM', 4)).to.be.NaN;
    expect(calculateNumber('SUM', 1, 2, 3)).to.equal(3);
  });
  it('sum two integers', () => {
    expect(calculateNumber('SUM', 1, 3)).to.equal(4);
  });
  it('sum of integer and float rounded above', () => {
    expect(calculateNumber('SUM', 1, 3.7)).to.equal(5);
  });
  it('sum of float rounded below and integer', () => {
    expect(calculateNumber('SUM', 2.3, 4)).to.equal(6);
  });
  it('sum two floats', () => {
    expect(calculateNumber('SUM', 1.2, 3.7)).to.equal(5);
  });
  it('sum with zero', () => {
    expect(calculateNumber('SUM', 1.6, 0)).to.equal(2);
    expect(calculateNumber('SUM', 0.3, 0)).to.equal(0);
  });
  it('sum two negative numbers', () => {
    expect(calculateNumber('SUM', -1.9, -7.7)).to.equal(-10);
  });
});

describe('test_chai_substract_calculateNumber', () => {
  it('substract with different number of arguments', () => {
    expect(calculateNumber()).to.equal(undefined);
    expect(calculateNumber('SUBTRACT', 4)).to.be.NaN;
    expect(calculateNumber('SUBTRACT', 4, 2, 3)).to.equal(2);
  });
  it('substract two integers', () => {
    expect(calculateNumber('SUBTRACT', 5, 3)).to.equal(2);
  });
  it('substract of integer and float rounded above', () => {
    expect(calculateNumber('SUBTRACT', 4, 3.7)).to.equal(0);
  });
  it('substract of float rounded below and integer', () => {
    expect(calculateNumber('SUBTRACT', 5.3, 2)).to.equal(3);
  });
  it('substract two floats', () => {
    expect(calculateNumber('SUBTRACT', 6.2, 4.4)).to.equal(2);
  });
  it('substract with zero', () => {
    expect(calculateNumber('SUBTRACT', 3, 0)).to.equal(3);
    expect(calculateNumber('SUBTRACT', 0.2, 0)).to.equal(0);
  });
  it('substract two negative numbers', () => {
    expect(calculateNumber('SUBTRACT', -3.9, -1.2)).to.equal(-3);
  });
});

describe('test_chai_divide_calculateNumber', () => {
  it('divide with different number of arguments', () => {
    expect(calculateNumber()).to.equal(undefined);
    expect(calculateNumber('DIVIDE', 4)).to.be.NaN;
    expect(calculateNumber('DIVIDE', 1.8, 2, 5)).to.equal(1);
  });
  it('divide two integers', () => {
    expect(calculateNumber('DIVIDE', 6, 3)).to.equal(2);
  });
  it('divide of integer and float rounded above', () => {
    expect(calculateNumber('DIVIDE', 9, 2.7)).to.equal(3);
  });
  it('divide of float rounded below and integer', () => {
    expect(calculateNumber('DIVIDE', 8.3, 4)).to.equal(2);
  });
  it('divide two floats', () => {
    expect(calculateNumber('DIVIDE', 5.7, 2.8)).to.equal(2);
  });
  it('divide with zero', () => {
    expect(calculateNumber('DIVIDE', 1.6, 0)).to.equal('Error');
    expect(calculateNumber('DIVIDE', 0, 8)).to.equal(0);
  });
  it('divide two negative numbers', () => {
    expect(calculateNumber('DIVIDE', -7.9, -3.7)).to.equal(2);
  });
});

describe('test__chai_type_calculateNumber', () => {
  it('if type of first argument is different of SUM, SUBSTRACT, DIVIDE', () => {
    expect(calculateNumber('POW', 2, 3)).to.equal(undefined);
  });
});
