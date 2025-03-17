import unittest
from unittest.mock import patch
import io
import sys


class TestEx1(unittest.TestCase):
    
    @patch('builtins.input', side_effect=['10', '20', '30'])
    def test_entrees_positives(self, mock_input):
        """Test avec des nombres positifs"""
        # Rediriger stdout pour capturer l'output
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        # Exécuter le code
        try:
            exec(open('../../tp1/ex1.py').read())
        except SystemExit:
            pass
        
        # Restaurer stdout
        sys.stdout = sys.__stdout__
        
        # Analyser l'output
        output = captured_output.getvalue()
        self.assertIn("Le maximum des trois nombres est: 30.0", output)
        self.assertIn("Le minimum des trois nombres est: 10.0", output)
        self.assertIn("La moyenne des trois nombres est: 20.00", output)
    
    @patch('builtins.input', side_effect=['-10', '-20', '-30'])
    def test_entrees_negatives(self, mock_input):
        """Test avec des nombres négatifs"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        try:
            exec(open('../../tp1/ex1.py').read())
        except SystemExit:
            pass
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertIn("Le maximum des trois nombres est: -10.0", output)
        self.assertIn("Le minimum des trois nombres est: -30.0", output)
        self.assertIn("La moyenne des trois nombres est: -20.00", output)
    
    @patch('builtins.input', side_effect=['5', '5', '5'])
    def test_entrees_identiques(self, mock_input):
        """Test avec des nombres identiques"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        try:
            exec(open('../../tp1/ex1.py').read())
        except SystemExit:
            pass
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertIn("Le maximum des trois nombres est: 5.0", output)
        self.assertIn("Le minimum des trois nombres est: 5.0", output)
        self.assertIn("La moyenne des trois nombres est: 5.00", output)


    @patch('builtins.input', side_effect=['1.5', '2.5', '3.5'])
    def test_entrees_decimales(self, mock_input):
        """Test avec des nombres décimaux"""
        captured_output = io.StringIO()
        sys.stdout = captured_output
        
        try:
            exec(open('../../tp1/ex1.py').read())
        except SystemExit:
            pass
        
        sys.stdout = sys.__stdout__
        output = captured_output.getvalue()
        
        self.assertIn("Le maximum des trois nombres est: 3.5", output)
        self.assertIn("Le minimum des trois nombres est: 1.5", output)
        self.assertIn("La moyenne des trois nombres est: 2.50", output)