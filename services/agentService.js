// /services/agentService.js

const db = require("../db");
const { v4: uuidv4 } = require("uuid");

class AgentService {
  async createAgent({ ownerId, type, config }) {
    const agent = {
      id: uuidv4(),
      ownerId,
      type,
      config,
      createdAt: new Date(),
      updatedAt: new Date(),
      status: "active",
    };
    await db.insert("agents", agent);
    return agent;
  }

  async getAgentById(id) {
    return db.findOne("agents", { id });
  }

  async updateAgent(id, updates) {
    updates.updatedAt = new Date();
    await db.update("agents", id, updates);
    return this.getAgentById(id);
  }

  async deleteAgent(id) {
    await db.delete("agents", id);
  }
}

module.exports = new AgentService();
