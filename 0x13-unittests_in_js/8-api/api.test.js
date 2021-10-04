const chai = require('chai');
const { expect } = require('chai');
const request = require('request');

describe('route GET /', () => {
  describe('GET', () => {
    const params = {
      url: 'https://localhost:7865',
      method: 'GET',
      }

    it('test for response of get request', (done) => {      
      request(params, function(error, response, body) {
        expect(response.statusCode).to.equal(200);
        expect(body).to.equal('Welcome to the payment system');
      });
    });
  });
});
