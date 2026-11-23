# import unittest
#
#
# class Person:
#     def __init__(self, first_name, last_name, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#
#     def get_full_name(self):
#         return f'{self.first_name} {self.last_name}'
#
#     def get_info(self):
#         return f'{self.first_name} {self.last_name} is {self.age} years old'
#
# class PersonTests(unittest.TestCase):
#     def setUp(self):
#         self.person = Person("Luc", "Peterson", 25)
#     def test_get_full_name(self):
#         result = self.person.get_full_name()
#         expected_result = "Luc Peterson"
#         self.assertEqual(result, expected_result)
#     def test_get_info(self):
#         result = self.person.get_info()
#         expected_result = "Luc Peterson is 25 years old"
#         self.assertEqual(result, expected_result)
# if __name__ == "__main__":
#     unittest.main()

from unittest import TestCase, main

from project.hero import Hero


class HeroTest(TestCase):
    username = "Test Hero"
    level = 5
    health = 18.9
    damage = 24.3

    def setUp(self) -> None:
        self.hero = Hero(self.username, self.level, self.health, self.damage)

    def test_init(self):
        self.assertEqual(self.hero.username, "Test Hero")
        self.assertEqual(self.hero.health, 18.9)
        self.assertEqual(self.hero.level, 5)
        self.assertEqual(self.hero.damage, 24.3)

    def test_battle_enemy_hero_has_the_same_name(self):
        enemy = Hero(self.username, self.level, self.health, self.damage)
        with self.assertRaises(Exception) as e:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight yourself", str(e.exception))

    def test_battle_hero_health_is_zero_raises_value_error(self):
        self.hero.health = 0
        enemy = Hero("Enemy", 5, 100, 10)
        with self.assertRaises(ValueError) as e:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(e.exception))

    def test_battle_hero_health_is_negative_raises_value_error(self):
        self.hero.health = -5
        enemy = Hero("Enemy", 5, 100, 10)
        with self.assertRaises(ValueError) as e:
            self.hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(e.exception))

    def test_battle_enemy_health_is_zero_raises_value_error(self):
        enemy = Hero("Enemy", 5, 0, 10)
        with self.assertRaises(ValueError) as e:
            self.hero.battle(enemy)
        self.assertEqual(f"You cannot fight {enemy.username}. He needs to rest", str(e.exception))

    def test_battle_enemy_health_is_negative_raises_value_error(self):
        enemy = Hero("Enemy", 5, -10, 10)
        with self.assertRaises(ValueError) as e:
            self.hero.battle(enemy)
        self.assertEqual(f"You cannot fight {enemy.username}. He needs to rest", str(e.exception))

    def test_battle_draw(self):
        # Създаваме герои с такива параметри, че да се победят взаимно едновременно
        hero = Hero("Hero", 1, 10, 10)
        enemy = Hero("Enemy", 1, 10, 10)
        result = hero.battle(enemy)
        self.assertEqual(result, "Draw")

    def test_battle_you_win(self):
        # Наш герой с голяма сила срещу слаб враг
        hero = Hero("Hero", 5, 100, 50)
        enemy = Hero("Enemy", 1, 10, 1)
        result = hero.battle(enemy)
        self.assertEqual(result, "You win")
        self.assertEqual(hero.level, 6)
        self.assertEqual(hero.health, 100 - 1 + 5)  # Здравето намалява от удара на врага, после се вдига с 5
        self.assertEqual(hero.damage, 55)

    def test_battle_you_lose(self):
        # Наш герой слаб срещу силен враг
        hero = Hero("Hero", 1, 10, 1)
        enemy = Hero("Enemy", 5, 100, 50)
        result = hero.battle(enemy)
        self.assertEqual(result, "You lose")
        self.assertEqual(enemy.level, 6)
        self.assertEqual(enemy.health, 100 - 1 + 5)
        self.assertEqual(enemy.damage, 55)

    def __str__(self):
        return f"Hero {self.username}: {self.level} lvl\n" \
               f"Health: {self.health}\n" \
               f"Damage: {self.damage}\n"

    def test_str_representation(self):
        expected = f"Hero {self.hero.username}: {self.hero.level} lvl\n" \
                   f"Health: {self.hero.health}\n" \
                   f"Damage: {self.hero.damage}\n"
        self.assertEqual(str(self.hero), expected)


if __name__ == "__main__":
    main()