import unittest
from modules.port_scanner import parse_ports

class TestPorts(unittest.TestCase):
    def test_single_and_range(self):
        self.assertEqual(parse_ports("22,80-82"), [22,80,81,82])

    def test_invalid(self):
        with self.assertRaises(ValueError):
            parse_ports("0")

if __name__ == "__main__":
    unittest.main()
