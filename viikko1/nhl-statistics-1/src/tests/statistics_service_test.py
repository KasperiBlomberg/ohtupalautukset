import unittest
from statistics_service import StatisticsService
from player import Player
from statistics_service import SortBy

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
        player = self.stats.search("Kurri")
        self.assertAlmostEqual(player.name, "Kurri")

    def test_search_None(self):
        player = self.stats.search("Kurrii")
        self.assertAlmostEqual(player, None)

    def test_team(self):
        players = self.stats.team("EDM")
        self.assertAlmostEqual(len(players), 3)

    def test_top_points(self):
        players = self.stats.top(1, SortBy.POINTS)
        self.assertAlmostEqual(len(players), 2)
        self.assertAlmostEqual(players[0].name, "Gretzky")
        self.assertAlmostEqual(players[1].name, "Lemieux")

    def test_top_goals(self):
        players = self.stats.top(1, SortBy.GOALS)
        self.assertAlmostEqual(len(players), 2)
        self.assertAlmostEqual(players[0].goals, 45)
        self.assertAlmostEqual(players[1].goals, 42)

    def test_top_assists(self):
        players = self.stats.top(1, SortBy.ASSISTS)
        self.assertAlmostEqual(len(players), 2)
        self.assertAlmostEqual(players[0].assists, 89)
        self.assertAlmostEqual(players[1].assists, 56)