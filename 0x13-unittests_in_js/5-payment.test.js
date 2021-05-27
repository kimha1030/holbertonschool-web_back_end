const { expect } = require('chai');
const sinon = require('sinon');
const utils = require('./utils');
const sendPaymentRequestToApi = require('./5-payment');

describe('test_payment', () => {
  let conLog;
  beforeEach(() => {
    conLog = sinon.spy(console, 'log');
  });
  it('test_payment_with_args_100_20', () => {
    sendPaymentRequestToApi(100, 20);
    expect(conLog.calledOnce).to.be.true;
    expect(conLog.calledOnceWithExactly('The total is: 120')).to.be.true;
  });
  it('test_payment_with_args_10_10', () => {
    sendPaymentRequestToApi(10, 10);
    expect(conLog.calledOnce).to.be.true;
    expect(conLog.calledOnceWithExactly('The total is: 20')).to.be.true;
  });
  afterEach(() => {
    conLog.restore();
  });
});
