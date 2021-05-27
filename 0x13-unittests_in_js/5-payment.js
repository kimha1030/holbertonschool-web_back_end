const utils = require('./utils');

module.exports = function sendPaymentRequestToApi(totalAmount, totalShipping) {
  const res = utils.calculateNumber('SUM', totalAmount, totalShipping);
  console.log(`The total is: ${res}`);
};
