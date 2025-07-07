"""
Modulo: test_suite.py
Test automatici unitari/funzionali per Massimo AI: garantisce che ogni modulo funzioni, nessuna regressione o bug dopo update.
Pronto per pytest/unittest, può essere ampliato con nuovi test a ogni release.
"""

import unittest
import data_manager
import agents
import feedback
import log_audit

class TestMassimoAI(unittest.TestCase):
    def test_add_user(self):
        data_manager.add_user(999, "TestUser", "Palermo", "Luca", "Prospect")
        user = data_manager.get_user_data(1)
        self.assertIsNotNone(user)

    def test_agent_motivazionale(self):
        response = agents.dispatch_agent("motivazionale", "Come posso essere più produttivo?", {"level": "base", "name": "Max"})
        self.assertTrue(isinstance(response, str) and len(response) > 0)

    def test_log_action(self):
        log_audit.log_action(999, "test", "test action")
        log = log_audit.get_audit_log()
        self.assertTrue(len(log) > 0)

    def test_feedback(self):
        feedback.collect_feedback(999, 8, "Va tutto bene!")
        feedbacks = feedback.get_feedbacks()
        self.assertTrue(len(feedbacks) > 0)

if __name__ == "__main__":
    unittest.main()
