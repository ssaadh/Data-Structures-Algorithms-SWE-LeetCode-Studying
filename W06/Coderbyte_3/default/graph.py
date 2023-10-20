from __future__ import annotations

# =============== BEGIN DO NOT MODIFY ========================
class Treasure:
    pass

class Monster:
    def __init__(self, name: str, damage: int):
        self.name = name 
        self.damage = damage 
        self.next = []

    def append_monster(self, monster):
        self.next.append(monster)

    def append_treasure(self, treasure: Treasure):
        self.next.append(treasure)

class Player:
    def __init__(self, health: int):
        self.health = health 
    
    def battle(self, monster: Monster):
        self.health -= monster.damage
# =============== END DO NOT MODIFY ========================

class Dungeon:
    def __init__(self, monster: Monster):
        self.monster = monster 

    # Is it possible for player to make it to the end if they start with infinite health?
    def can_at_least_one_path_make_it(self) -> bool:
        pass

    # Is it possible for player to make it to end without losing all their health? 
    def can_make_it(self, player: Player) -> bool:
        pass

    # Will any path make it to the end? Can they choose randomly and always make it?
    def can_all_paths_make_it(self, player: Player) -> bool:
        pass

    # If picking paths randomly, what is the probability player will make it to the end?
    def probability_player_will_make_it(self, player: Player) -> float:
        pass
