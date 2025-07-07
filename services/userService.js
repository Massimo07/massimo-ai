// /services/userService.js

const { v4: uuidv4 } = require("uuid");
const bcrypt = require("bcrypt");
const db = require("../db"); // presupposto: layer DB astratto

class UserService {
  async createUser({ email, password, name, role }) {
    const hashedPassword = await bcrypt.hash(password, 12);
    const user = {
      id: uuidv4(),
      email,
      password: hashedPassword,
      name,
      role: role || "user",
      createdAt: new Date(),
      updatedAt: new Date(),
    };
    await db.insert("users", user);
    return user;
  }

  async getUserByEmail(email) {
    return db.findOne("users", { email });
  }

  async getUserById(id) {
    return db.findOne("users", { id });
  }

  async updateUser(id, updates) {
    updates.updatedAt = new Date();
    await db.update("users", id, updates);
    return this.getUserById(id);
  }

  async deleteUser(id) {
    await db.delete("users", id);
  }

  async verifyPassword(email, plainPassword) {
    const user = await this.getUserByEmail(email);
    if (!user) return false;
    return bcrypt.compare(plainPassword, user.password);
  }
}

module.exports = new UserService();
