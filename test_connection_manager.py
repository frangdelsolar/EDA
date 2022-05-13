import unittest
from connection_manager import *
from challenge import Challenge
from connection_manager import ConnectionManager

class TestConnectionManager(unittest.TestCase):

    def test_append_challenge(self):
        connection = ConnectionManager()
        self.assertEqual(len(connection.challenges), 0)

        connection.append_challenge(123)
        connection.append_challenge(124)
        self.assertEqual(len(connection.challenges), 2)

    def test_get_or_create_challenge(self):
        chosen_id = '124'
        connection = ConnectionManager()
        connection.append_challenge('123')
        connection.append_challenge(chosen_id)
        connection.append_challenge('127')
        chosen_challenge = connection.get_or_create_challenge(chosen_id)
        self.assertEqual(chosen_challenge.id, chosen_id)


if __name__ == '__main__':
    unittest.main()