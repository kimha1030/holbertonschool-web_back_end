const chai = require('chai');
const { expect } = require('chai');
const request = require('request');

describe('route GET /', () => {
  it('test for response of get request', () => {
    const params = {
      url: 'https://localhost:7865',
      method: 'GET',
    };
    request(params, (_error, response, body) => {
      expect(response.statusCode).to.equal(200);
      expect(body).to.equal('Welcome to the payment system');
    });
  });
});
