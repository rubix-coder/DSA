# from abc import ABC, abstractmethod


# # 1. Define the Abstract Class (The Blueprint)
# class Enemy(ABC):

#   @abstractmethod
#   def attack(self):
#     """Every enemy MUST implement how it attacks."""
#     pass

#   def __or__(self, other):
#     """Lets `enemyA.attack() | enemyB.attack()` read like a DAG pipe:
#     combine two enemies into a single squad that attacks together."""
#     print(f"-> {self.__class__.__name__} and {other.__class__.__name__} attack together!")
#     return Squad(self, other)


# class Squad(Enemy):
#   """Result of `|`-combining enemies. A Squad is itself an Enemy, so
#   the chain can keep growing: a | b | c."""

#   def __init__(self, *members):
#     self.members = members

#   def attack(self):
#     for m in self.members:
#       m.attack()
#     return self


# # 2. Try to instantiate the abstract class directly -> ERROR
# # enemy = Enemy()  # TypeError: Can't instantiate abstract class Enemy


# # 3. Create a concrete class WITHOUT implementing attack() -> ERROR
# class Robot(Enemy):
#       def attack(self):
#          print("Robot Attack")
#          return self  # returning self is what makes `| ` chainable


# bot = Robot()

# # 4. Correct Implementation
# class Zombie(Enemy):

#   def attack(self):
#     print("Zombie bites for 10 damage!")
#     return self


# zombie = Zombie()


# squad = bot.attack() | zombie.attack()
# squad.attack()  # re-runs both members through the Squad

import random
class Contains:
    def __contains__(self, item):
        print(f"in{self,item}")
        return True if item in range(100) else False

    c = __contains__(random.randint(0,100),10)
    print(c)

if __name__=="__main__":
    isCont = Contains()
    randval = random.randint(0,120)
    print(randval)
    print("Is presnet") if randval in isCont else print("Is Absent")