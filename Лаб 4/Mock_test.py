import unittest
import sys, os
from unittest.mock import patch, Mock

import builder

sys.path.append(os.getcwd())
from builder import *

class Computer_Builder_Test(unittest.TestCase):
    @patch.object(builder.Computer_Builder(), 'Videocard')
    def test_videcard(self, mock_videocard):
        mock_videocard.return_value = None
        self.assertEqual(Computer_Builder().videocard(), None)
