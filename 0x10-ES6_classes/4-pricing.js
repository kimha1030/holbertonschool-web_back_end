import Currency from './3-currency';

class Pricing {
  constructor(amount, currency) {
    this._amount = amount;
    this._currency = currency;
  }

  set amount(amount) {
    this._amount = amount;
  }

  get amount() {
    return this._amount;
  }

  set currency(currency) {
    if (currency instanceof Currency) {
      this._currency = currency;
    }
  }

  get currency() {
    return this._currency;
  }

  displayFullPrice() {
    return `${this._amount} ${this._currency.name} (${this._currency.code})`;
  }

  static convertPrice(amount, conversionRate) {
    return amount * conversionRate;
  }
}

export default Pricing;
