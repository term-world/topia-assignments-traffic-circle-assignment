import narrator
import random

from narrator.Checkpoint import check_flag, set_flag
from inventory.Item import FixtureSpec

class Stoplight(FixtureSpec):

  def __init__(self) -> None:
    super().__init__()
    flag = check_flag("northeast_light")
    self.state = flag if flag else "🔴"
    self.crosswalk = "✋"
    self.pedestrians = 0 + check_flag("northeast_wait")
    if self.state != "🔴":
      self.pedestrians += random.randint(1,5)

  def __str__(self) -> str:
    return f"{self.state} {self.crosswalk}"

  def use(self) -> None:
    # Do not alter
    light = self.state
    crosswalk = self.crosswalk
    people_waiting = self.pedestrians
    # Do not alter

    #----------------------)
    """
    TODO: Create stoplight functionality using directions, variables, and
          guidance from the README. This light uses:

          * light
          * crosswalk
          * people_waiting
    """
    #----------------------
    
    # Do not alter
    self.state = light
    self.crosswalk = crosswalk
    self.pedestrians = people_waiting
    set_flag("northeast_light",self.state)
    set_flag("northeast_wait",self.pedestrians)
    # Do not alter

def main():
  stoplight = Stoplight()
  stoplight.use()
  print(stoplight)

if __name__ == "__main__":
  main()