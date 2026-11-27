from project.soccer_player import SoccerPlayer
from unittest import TestCase, main


class SockerPlayerTest(TestCase):
    def setUp(self) -> None:
        self.player1 = SoccerPlayer("Test Player 1", 22, 250, "Barcelona")
        self.player2 = SoccerPlayer("Test Player 2", 32, 280, "PSG")

    def test_init_success(self):
        self.assertEqual("Test Player 1", self.player1.name)
        self.assertEqual(22, self.player1.age)
        self.assertEqual(250, self.player1.goals)
        self.assertEqual("Barcelona", self.player1.team)
        self.assertEqual({}, self.player1.achievements)

    def test_name_validation_raises_exception(self):
        with self.assertRaises(ValueError) as e:
            self.player1.name = "Test1"
        self.assertEqual("Name should be more than 5 symbols!", str(e.exception))

        with self.assertRaises(ValueError):
            SoccerPlayer("Short", 20, 10, "Barcelona")

    def test_age_validation_raises_exception(self):
        with self.assertRaises(ValueError) as e:
            self.player1.age = 15
        self.assertEqual("Players must be at least 16 years of age!", str(e.exception))

        with self.assertRaises(ValueError):
            SoccerPlayer("Valid Name", 15, 10, "Barcelona")

    def test_goals_validation_negative_sets_to_zero(self):
        self.player1.goals = -1
        self.assertEqual(0, self.player1.goals)

        player_neg = SoccerPlayer("Valid Name", 20, -5, "Barcelona")
        self.assertEqual(0, player_neg.goals)

    def test_team_validation_raises_exception(self):
        with self.assertRaises(ValueError) as e:
            self.player1.team = "Unknown"

        self.assertEqual(
            "Team must be one of the following: Barcelona, Real Madrid, Manchester United, Juventus, PSG!",
            str(e.exception)
        )

    def test_change_team_valid(self):
        result = self.player1.change_team("Real Madrid")
        self.assertEqual("Team successfully changed!", result)
        self.assertEqual("Real Madrid", self.player1.team)

    def test_change_team_invalid(self):
        result = self.player1.change_team("Arsenal")
        self.assertEqual("Invalid team name!", result)
        self.assertEqual("Barcelona", self.player1.team)

    def test_add_new_achievement(self):
        result = self.player1.add_new_achievement("Man of the Match")
        self.assertEqual("Man of the Match has been successfully added to the achievements collection!", result)
        self.assertEqual(1, self.player1.achievements["Man of the Match"])

        self.player1.add_new_achievement("Man of the Match")
        self.assertEqual(2, self.player1.achievements["Man of the Match"])

    def test_lt_operator(self):
        res1 = self.player1 < self.player2
        self.assertEqual("Test Player 2 is a top goal scorer! S/he scored more than Test Player 1.", res1)

        res2 = self.player2 < self.player1
        self.assertEqual("Test Player 2 is a better goal scorer than Test Player 1.", res2)


if __name__ == "__main__":
    main()