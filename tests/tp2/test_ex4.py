import io
import unittest
import sys
from unittest.mock import patch
from tp2 import ex4

sys.path.append('../../tp2')  # Ajouter le chemin vers les modules du TP2


class TestEx4(unittest.TestCase):

    def test_valeurs_aleatoires_dans_intervalles(self):
        """Test que les valeurs générées sont bien dans les intervalles spécifiés"""
        # Recharger le module pour obtenir de nouvelles valeurs aléatoires

        # Vérifier que reel1 est dans l'intervalle [0.1, 1.0]
        self.assertGreaterEqual(ex4.reel1, 0.1)
        self.assertLessEqual(ex4.reel1, 1.0)

        # Vérifier que reel2 est dans l'intervalle [3.5, 33.5]
        self.assertGreaterEqual(ex4.reel2, 3.5)
        self.assertLessEqual(ex4.reel2, 33.5)

    @patch('random.uniform', side_effect=[0.5, 15.0])
    def test_appel_function_random(self, mock_uniform):
        """Test que la fonction random.uniform est bien appelée avec les bons paramètres"""
        # Capturer la sortie standard
        captured_output = io.StringIO()
        sys.stdout = captured_output

        try:
            exec(open('../../tp2/ex4.py').read())
        except SystemExit:
            pass

        # Restaurer la sortie standard
        sys.stdout = sys.__stdout__

        # Vérifier que la fonction random.uniform a été appelée avec les bons paramètres
        mock_uniform.assert_any_call(0.1, 1.0)
        mock_uniform.assert_any_call(3.5, 33.5)

        # Vérifier l'affichage de la somme des éléments
        output = captured_output.getvalue()
        self.assertIn('15.5', output)