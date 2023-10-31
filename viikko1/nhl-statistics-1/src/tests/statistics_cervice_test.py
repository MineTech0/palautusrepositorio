import unittest
from statistics_service import StatisticsService
from player import Player
from sort_by import SortBy

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatisticsService(unittest.TestCase):
    def setUp(self):
        # annetaan StatisticsService-luokan oliolle "stub"-luokan olio
        self.stats = StatisticsService(
            PlayerReaderStub()
        )
        
    def test_search(self):
        player = self.stats.search("Semenko")
        self.assertEqual(player.name, "Semenko")

        player = self.stats.search("Gretzky")
        self.assertEqual(player.name, "Gretzky")

        player = self.stats.search("Selanne")
        self.assertIsNone(player)
        
    def test_team(self):
        players = self.stats.team("EDM")
        self.assertEqual(len(players), 3)

        players = self.stats.team("PIT")
        self.assertEqual(len(players), 1)

        players = self.stats.team("DET")
        self.assertEqual(len(players), 1)

        players = self.stats.team("COL")
        self.assertEqual(len(players), 0)
    
    def test_top(self):
        players = self.stats.top(3)
        self.assertEqual(len(players), 4)
        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Lemieux")
        self.assertEqual(players[2].name, "Yzerman")
        self.assertEqual(players[3].name, "Kurri")
        
    def test_top_assists(self):
        players = self.stats.top(3, SortBy.ASSISTS)
        self.assertEqual(len(players), 4)
        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Yzerman")
        self.assertEqual(players[2].name, "Lemieux")
        self.assertEqual(players[3].name, "Kurri")
        
    def test_top_goals(self):
        players = self.stats.top(3, SortBy.GOALS)
        self.assertEqual(len(players), 4)
        self.assertEqual(players[0].name, "Lemieux")
        self.assertEqual(players[1].name, "Yzerman")
        self.assertEqual(players[2].name, "Kurri")
        self.assertEqual(players[3].name, "Gretzky")
    
    def test_top_points(self):
        players = self.stats.top(3, SortBy.POINTS)
        self.assertEqual(len(players), 4)
        self.assertEqual(players[0].name, "Gretzky")
        self.assertEqual(players[1].name, "Lemieux")
        self.assertEqual(players[2].name, "Yzerman")
        self.assertEqual(players[3].name, "Kurri")