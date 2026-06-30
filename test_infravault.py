# test_infravault.py
"""
Tests for InfraVault module.
"""

import unittest
from infravault import InfraVault

class TestInfraVault(unittest.TestCase):
    """Test cases for InfraVault class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = InfraVault()
        self.assertIsInstance(instance, InfraVault)
        
    def test_run_method(self):
        """Test the run method."""
        instance = InfraVault()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
