// /services/worldService.js

const db = require("../db");
const { v4: uuidv4 } = require("uuid");

class WorldService {
  async createWorld({ ownerId, name, description, config }) {
    const world = {
      id: uuidv4(),
      ownerId,
      name,
      description,
      config,
      createdAt: new Date(),
      updatedAt: new Date(),
    };
    await db.insert("worlds", world);
    return world;
  }

  async getWorldById(id) {
    return db.findOne("worlds", { id });
  }

  async updateWorld(id, updates) {
    updates.updatedAt = new Date();
    await db.update("worlds", id, updates);
    return this.getWorldById(id);
  }

  async deleteWorld(id) {
    await db.delete("worlds", id);
  }
}

module.exports = new WorldService();
