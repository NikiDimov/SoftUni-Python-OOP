from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero('Niki', 1, 100, 10)

    def test_initialization(self):
        self.assertEqual('Niki', self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(10, self.hero.damage)

    def test_battle_against_myself_raises(self):
        enemy = Hero('Niki', 2, 200, 30)
        with self.assertRaises(Exception) as ex:
            self.hero.battle(enemy)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_without_health(self):
        hero = Hero("Niki", 1, 0, 30)
        enemy = Hero('Misho', 2, 200, 30)
        with self.assertRaises(ValueError) as ex:
            hero.battle(enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ex.exception))

    def test_battle_enemy_with_no_health(self):
        hero = Hero("Niki", 1, 10, 30)
        enemy = Hero('Misho', 2, 0, 30)
        with self.assertRaises(ValueError) as ex:
            hero.battle(enemy)
        self.assertEqual("You cannot fight Misho. He needs to rest", str(ex.exception))

    def test_battle_with_draw(self):
        hero = Hero("Niki", 1, 20, 30)
        enemy = Hero('Misho', 1, 30, 30)
        self.assertEqual("Draw", hero.battle(enemy))

    def test_battle_hero_wins(self):
        hero = Hero("Niki", 1, 200, 30)
        enemy = Hero('Misho', 1, 30, 30)
        self.assertEqual("You win", hero.battle(enemy))
        self.assertEqual(2, hero.level)
        self.assertEqual(175, hero.health)
        self.assertEqual(35, hero.damage)

    def test_hero_loses(self):
        hero = Hero("Niki", 1, 30, 30)
        enemy = Hero('Misho', 1, 200, 30)
        self.assertEqual("You lose", hero.battle(enemy))
        self.assertEqual(2, enemy.level)
        self.assertEqual(175, enemy.health)
        self.assertEqual(35, enemy.damage)

    def test_str_representation_of_hero(self):
        self.assertEqual("Hero Niki: 1 lvl\nHealth: 100\nDamage: 10\n", str(self.hero))
        






if __name__ == '__main__':
    main()
