from RPSLS_player import RPSLS_player

class P15557(RPSLS_player):
  def __init__(self):
    pass

  def shoot(self):
    import random
    return random.choice(["Rock","Paper", "Scissor", "Lizard", "Spark"])

  def update(self, result: str, competitor_shot: str):
    pass