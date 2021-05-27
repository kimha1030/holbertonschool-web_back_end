const { expect } = require('chai');
const sinon = require('sinon');
const utils = require('./utils');
const sendPaymentRequestToApi = require('./3-payment');

describe('test_payment', () => {
  it('usage of the Utils function', () => {
    const spyCalculateNum = sinon.spy(utils, 'calculateNumber');
    const conLog = sinon.spy(console, 'log');
    sendPaymentRequestToApi(100, 20);
    expect(spyCalculateNum.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
    spyCalculateNum.restore();
    expect(conLog.calledOnceWithExactly('The total is: 120')).to.be.true;
    conLog.restore();
    expect(utils.calculateNumber('SUM', 100, 20)).to.equal(120);
  });
});
