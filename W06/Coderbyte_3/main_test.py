from __future__ import annotations
import unittest
from graph import Monster, Treasure, Player, Dungeon

class GraphTest(unittest.TestCase):

    # a(3) -> b(4) -> c(5) -> treasure
    def create_dungeon(self) -> Dungeon:
        a = Monster("a", 3)
        b = Monster("b", 4)
        c = Monster("c", 5)
        treasure = Treasure()
        a.append_monster(b)
        b.append_monster(c)
        c.append_treasure(treasure)

        return Dungeon(a)

    # a(3) -> b(4)  c(5) -> treasure
    def create_dungeon2(self) -> Dungeon:
        a = Monster("a", 3)
        b = Monster("b", 4)
        c = Monster("c", 5)
        treasure = Treasure()
        a.append_monster(b)
        c.append_treasure(treasure)

        return Dungeon(a)

    # a(1) -> b(4)
    #   |      |
    #   v      v
    # c(2) -> d(1) -> treasure
    def create_dungeon3(self):
        a = Monster("a", 1)
        b = Monster("b", 4)
        c = Monster("c", 2)
        d = Monster("d", 1)
        treasure = Treasure()
        a.append_monster(b)
        a.append_monster(c)
        b.append_monster(d)
        c.append_monster(d)
        d.append_treasure(treasure)

        return Dungeon(a)

    # a(1) -> b(4) -> e(1)
    #   |      |
    #   v      v
    # c(2) -> d(1) -> treasure

    '''
    Probability review: Just because there are 2 different possiblilites does not 
    mean that they are equal probability. For example, on any given day, there could be 
    rain or no rain. That doesn't imply that rain has a 50% chance.

    In this case, there are 3 different paths:
    a->c->d->treasure, a->b->d->treasure, and a->b->e. 
    
    Here, a->c->d->tresure has a 50% chance of happening, a->b->e is 25%, and a->b->d->treasure is 25%. 
    An easy way to think about it that the probability of A reaching C is 50% and C reaching D is 100%
    and D reaching Treasure is 100%. Overall, it would be 50% chance to do A->C->D->Treasure.
    '''
    def create_dungeon4(self):
        a = Monster("a", 1)
        b = Monster("b", 4)
        c = Monster("c", 2)
        d = Monster("d", 1)
        e = Monster("e", 1)
        treasure = Treasure()
        a.append_monster(b)
        a.append_monster(c)
        b.append_monster(d)
        c.append_monster(d)
        b.append_monster(e)
        d.append_treasure(treasure)

        return Dungeon(a)

    # a(1) -> b(5) -> e(1) 
    #   |      |       |       
    #   v      v       v        
    # c(2) -> d(7) -> f(2) -> treasure
    # optimal -> a -> b -> e -> f
    def create_dungeon5(self):
        a = Monster("a", 1)
        b = Monster("b", 5)
        c = Monster("c", 2)
        d = Monster("d", 7)
        e = Monster("e", 1)
        f = Monster("f", 2)
        treasure = Treasure()
        a.append_monster(b)
        a.append_monster(c)
        b.append_monster(e)
        b.append_monster(d)
        c.append_monster(d)
        d.append_monster(f)
        e.append_monster(f)
        f.append_treasure(treasure)

        return Dungeon(a)

    # a(1) -> b(5) -> e(1) ------
    #   |      |       |        |
    #   v      v       v        v
    # c(2) -> d(7) -> f(2) -> treasure
    # optimal -> a -> b -> e -> f
    def create_dungeon6(self):
        a = Monster("a", 1)
        b = Monster("b", 5)
        c = Monster("c", 2)
        d = Monster("d", 7)
        e = Monster("e", 1)
        f = Monster("f", 2)
        treasure = Treasure()
        a.append_monster(b)
        a.append_monster(c)
        b.append_monster(e)
        b.append_monster(d)
        c.append_monster(d)
        d.append_monster(f)
        e.append_monster(f)
        e.append_treasure(treasure)
        f.append_treasure(treasure)

        return Dungeon(a)

    def test_can_at_least_one_path_make_it(self):
        dungeon = self.create_dungeon()
        self.assertEqual(dungeon.can_at_least_one_path_make_it(), True)
        
        dungeon = self.create_dungeon2()
        self.assertEqual(dungeon.can_at_least_one_path_make_it(), False)


    def test_can_all_paths_make_it(self):
        dungeon = self.create_dungeon()
        self.assertEqual(dungeon.can_all_paths_make_it(Player(11)), False)

        dungeon = self.create_dungeon()
        self.assertEqual(dungeon.can_all_paths_make_it(Player(12)), True)

        dungeon = self.create_dungeon2()
        self.assertEqual(dungeon.can_all_paths_make_it(Player(7)), False)
        
        dungeon = self.create_dungeon3()
        self.assertEqual(dungeon.can_all_paths_make_it(Player(5)), False)

        dungeon = self.create_dungeon3()
        self.assertEqual(dungeon.can_all_paths_make_it(Player(6)), True)
   
        dungeon = self.create_dungeon4()
        self.assertEqual(dungeon.can_all_paths_make_it(Player(100)), False)

    def test_probability_player_will_make_it(self):
        dungeon = self.create_dungeon()
        self.assertEqual(dungeon.probability_player_will_make_it(Player(12)), 1.0)

        dungeon = self.create_dungeon()
        self.assertEqual(dungeon.probability_player_will_make_it(Player(11)), 0.0)
        
        dungeon = self.create_dungeon2()
        self.assertEqual(dungeon.probability_player_will_make_it(Player(100)), 0.0)

        dungeon = self.create_dungeon3()
        self.assertEqual(dungeon.probability_player_will_make_it(Player(1)), 0.0)

        dungeon = self.create_dungeon3()
        self.assertEqual(dungeon.probability_player_will_make_it(Player(5)), 0.5)

        dungeon = self.create_dungeon3()
        self.assertEqual(dungeon.probability_player_will_make_it(Player(100)), 1.0)

        dungeon = self.create_dungeon4()
        self.assertEqual(dungeon.probability_player_will_make_it(Player(1)), 0.0)

        dungeon = self.create_dungeon4()
        self.assertEqual(dungeon.probability_player_will_make_it(Player(5)), 0.5)

        dungeon = self.create_dungeon4()
        self.assertEqual(dungeon.probability_player_will_make_it(Player(100)), 0.75)

    def test_can_make_it(self):
        dungeon = self.create_dungeon5()
        self.assertEqual(dungeon.can_make_it(Player(9)), True)

        dungeon = self.create_dungeon5()
        self.assertEqual(dungeon.can_make_it(Player(8)), False)

        dungeon = self.create_dungeon6()
        self.assertEqual(dungeon.can_make_it(Player(7)), True)

        dungeon = self.create_dungeon6()
        self.assertEqual(dungeon.can_make_it(Player(6)), False)