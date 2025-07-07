// /services/paymentService.js

const db = require("../db");
const stripe = require("stripe")(process.env.STRIPE_SECRET_KEY);

class PaymentService {
  async createPaymentIntent(amount, currency = "eur") {
    return stripe.paymentIntents.create({
      amount,
      currency,
      payment_method_types: ["card"],
    });
  }

  async confirmPayment(paymentIntentId) {
    return stripe.paymentIntents.confirm(paymentIntentId);
  }

  async recordPayment(paymentData) {
    await db.insert("payments", paymentData);
  }

  async getUserPayments(userId) {
    return db.find("payments", { userId });
  }
}

module.exports = new PaymentService();
