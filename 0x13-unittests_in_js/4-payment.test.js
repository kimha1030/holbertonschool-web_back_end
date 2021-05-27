const { expect } = require('chai');
const sinon = require('sinon');
const utils = require('./utils');
const sendPaymentRequestToApi = require('./4-payment');

describe('test_payment', () => {
  it('usage of the Utils function', () => {
    const stubCalculateNum = sinon.stub(utils, 'calculateNumber').returns(10);
    const conLog = sinon.spy(console, 'log');
    sendPaymentRequestToApi(100, 20);
    expect(stubCalculateNum.calledOnceWithExactly('SUM', 100, 20)).to.be.true;
    stubCalculateNum.restore();
    expect(conLog.calledOnceWithExactly('The total is: 10')).to.be.true;
    conLog.restore();
  });
});
