const { expect } = require('chai');
const sinon = require('sinon');
const getPaymentTokenFromAPI = require('./6-payment_token');

describe('getPaymentTokenFromAPI', () => {
  it('if getPaymentTokenFromAPI(true)', () => new Promise((done) => {
    getPaymentTokenFromAPI(true)
      .then((res) => {
        expect(res).to.equal({ data: 'Successful response from the API' });
        done();
      })
      .catch((e) => {
        done(e);
      });
  }));
});
