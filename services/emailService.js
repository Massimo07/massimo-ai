// /services/emailService.js

const nodemailer = require("nodemailer");

class EmailService {
  constructor() {
    this.transporter = nodemailer.createTransport({
      host: process.env.SMTP_HOST,
      port: parseInt(process.env.SMTP_PORT) || 587,
      secure: false, // true per 465, false per altri
      auth: {
        user: process.env.SMTP_USER,
        pass: process.env.SMTP_PASS,
      },
    });
  }

  async sendEmail(to, subject, html) {
    const mailOptions = {
      from: `"Massimo AI" <${process.env.SMTP_USER}>`,
      to,
      subject,
      html,
    };

    return this.transporter.sendMail(mailOptions);
  }
}

module.exports = new EmailService();
