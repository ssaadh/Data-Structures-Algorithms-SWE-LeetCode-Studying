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

from queue import Queue

class Dungeon:
  def __init__(self, monster: Monster):
    self.monster = monster 

  # Think of BFS as initial framework
  # Not worrying about health right now
  # need to check every path
  # Add self.monster to queue
  # Don't have to check if this Treasure because self.monster is type checked as a Monster
  # Add first next el to queue (FIFO so O(1) adding and removing from end like list)  
  # Add first next el to a visited data structure like set.  
  # Do while queue of el is empty. empty might go away so use qsize() == 0 to check for empty
  # go to first next el
  # check if it's treasure using function type or isinstance
  # if so, return True
  # check all of the neighbors of the el
  # check if it's Treasure in neighbor? Save going thru the queue!
  # if not visited, add to queue, add to visited
  # Return false outside the queue loop

  # Let's go thru dungeon 4:
  # Start with a:
  # queue = a
  # visited = a
  # neighors are b, c
  # queue = b, c
  # visited = a, b, c
  # b next
  # neighbors are d
  # queue = c, d
  # visited = a, b, c, d
  # c is next
  # neighbors are d. already in visited
  # queue = d
  # visited = a, b, c, d
  # d is next
  # neighbors are treasure
  # queue = treasure
  # visited = a, b, c, d, treasure

  # checking for visited doesn't make sense. Want to go thru all paths

  # Is it possible for player to make it to the end if they start with infinite health?
  def can_at_least_one_path_make_it(self) -> bool:
    queue = Queue()
    queue.put(self.monster)

    while queue.qsize() > 0:
      cur = queue.get()
      for neighbor in cur.next:
        if type(neighbor) is Treasure:
          return True
        queue.put(neighbor)
    return False

  # The above has to be adjusted to include seeing if subtracting health keeps health above 0.
  # in the queue loop, have the player battle the monster (player.battle(self.monster))
  # check if there is any health left. If not, return False

  # DFS might be better? But continuing with BFS
  # Have to track the entire path.
  # In the queue add a tuple of the path so far as a list and the player health
  # which requires including the player itself
  # when taking out from queue, take out the current path list and the player
  # check if player battle health keeps it at least at 0 from the last element of the path list
  # when checking neighbors, add the neighbor to the path list and queue the path list and player as a tuple

  # Whoops. Don't return False. Dont check the player health initially.
  # When checking to see if the current neighbor is Treasure also check if player health is not negative

  # Okay shit...i need to trace since Treasure is being tried in battle

  # The first time Treasure comes up before being added to the queue at all, it should end
  # Oh, if the player health is below 0, the Treasure will be appended.

  # LOL path is always appending everything. the paths arent being separate.
  # does the path have to be cloned each time?

  # Okay and the same player is being added to all of them.
  # Isn't this technically memory expensive carrying all this extra stuff since the player class has to be kept too?
  # Clearly we arent supposed to just track the health and subtract it on our own presumably.

  # 

  # Doing dungeon 5 and Player(9):
  # after neighbors:
  # queue = [([a, b], 8), ([a, c], 8)]
  # next up lowers health to 3.
  # after next queue e and d get added

  # No idea how to do this while also using player.battle method so won't do that any more.

  # Is it possible for player to make it to end without losing all their health? 
  def can_make_it(self, player: Player) -> bool:
    queue = Queue()
    queue.put(([self.monster], 0))
    while queue.qsize() > 0:
      path, playa = queue.get()
      playa += path[-1].damage

      for neighbor in path[-1].next:
        if type(neighbor) is Treasure:
          if playa <= player.health:
            return True
        else:
          new_path = path[:]
          new_path.append(neighbor)
          queue.put((new_path, playa))
    return False

  # Every path has to be checked so if there is no negative return in the loop, can return True outside the loop
  # A negative return is if there is treasure and too much damage has been taken
  # A path that doesnt reach the treasure is considered a failure too
  # Initial thinking is if there is no neighbor (no next), then can return False because the end of the path has no treasure

  # Will any path make it to the end? Can they choose randomly and always make it?
  def can_all_paths_make_it(self, player: Player) -> bool:
    queue = Queue()
    queue.put(([self.monster], 0))
    while queue.qsize() > 0:
      path, playa = queue.get()
      playa += path[-1].damage

      for neighbor in path[-1].next:
        if type(neighbor) is Treasure:
          if playa > player.health:
            return False
        else:
          new_path = path[:]
          new_path.append(neighbor)
          queue.put((new_path, playa))

      if len(path[-1].next) == 0:
         return False
    return True

  # Have to track all the ultimate paths. So above where each return or continue happens, that has to be tracked.
  # Divide the neighbors by 1. That is the percent. For each subsequent iteration, divide again and then multiple with the previous percent.
  # Can append the sum of the successful percentages and return that
  # Like before where I can't keep re-using the same variables, the percentage being calculated (in the neighbor loop) has to be a new variable each time so each neighbor gets its own correct percentage score.

  # We are only tracking winning percentages so dont need to care if no treasure is reached. That won't be increasing the probability.

  # If picking paths randomly, what is the probability player will make it to the end?
  def probability_player_will_make_it(self, player: Player) -> float:
    queue = Queue()
    final = 0.0
    # (monster, damage, percentage)
    queue.put(([self.monster], 0, 1.0))

    while queue.qsize() > 0:
      path, playa, percentage = queue.get()
      playa += path[-1].damage

      for neighbor in path[-1].next:
        percent = 1 / len(path[-1].next)
        new_percentage = percentage * percent

        if type(neighbor) is Treasure:
          if playa <= player.health:
            final += new_percentage
        else:
          new_path = path[:]
          new_path.append(neighbor)
          queue.put((new_path, playa, new_percentage))
    return final


  ## Utilities
  def print_queue(self, queue):
    a = []
    while queue.qsize > 0:
      path, playa = queue.get()
      a.append(path)
    for m in path:
      print(self.print_path(path))
    print(playa)
  
  def print_path(self, path):
    a = []
    for m in path:
      a.append(m.name)
    return a
