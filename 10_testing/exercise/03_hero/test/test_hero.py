from unittest import TestCase, main
from project.hero import Hero


class HeroTest(TestCase):
    def setUp(self) -> None:
        self.username = "Test Hero"
        self.level = 5
        self.health = 100.0
        self.damage = 25.0
        self.hero = Hero(self.username, self.level, self.health, self.damage)

    def test_init(self):
        self.assertEqual(self.hero.username, self.username)
        self.assertEqual(self.hero.level, self.level)
        self.assertEqual(self.hero.health, self.health)
        self.assertEqual(self.hero.damage, self.damage)

    def test_battle_cant_fight_yourself_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_hero_health_below_or_equal_zero_raises_value_error(self):
        self.hero.health = 0
        enemy = Hero("Enemy", 1, 100, 10)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

        self.hero.health = -10
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_enemy_health_below_or_equal_zero_raises_value_error(self):
        enemy = Hero("Enemy", 1, 0, 10)
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy)
        self.assertEqual(f"You cannot fight {enemy.username}. He needs to rest", str(ex.exception))

        enemy.health = -5
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(enemy)
        self.assertEqual(f"You cannot fight {enemy.username}. He needs to rest", str(ex.exception))

    def test_battle_draw(self):
        enemy = Hero("Enemy", 5, 125.0, 25.0)
        self.hero.health = 125.0
        result = self.hero.battle(enemy)
        self.assertEqual(result, "Draw")

    def test_battle_you_win(self):
        enemy = Hero("Enemy", 1, 50.0, 10.0)
        result = self.hero.battle(enemy)
        self.assertEqual(result, "You win")
        self.assertEqual(self.hero.level, 6)
        self.assertEqual(self.hero.health, 100.0 - 10.0 + 5.0)  # 95.0
        self.assertEqual(self.hero.damage, 30.0)

    def test_battle_you_lose(self):
        enemy = Hero("Enemy", 5, 200.0, 30.0)
        result = self.hero.battle(enemy)
        self.assertEqual(result, "You lose")
        self.assertEqual(enemy.level, 6)
        self.assertEqual(enemy.health, 200.0 - (25.0 * 5) + 5.0)  # 80.0
        self.assertEqual(enemy.damage, 35.0)

    def test_str_format(self):
        expected = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
                   f"Health: {self.hero.health}\n" \
                   f"Damage: {self.hero.damage}\n"
        self.assertEqual(str(self.hero), expected)


if __name__ == "__main__":
    main()