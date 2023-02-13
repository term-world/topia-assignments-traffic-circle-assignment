import narrator
import random

from narrator.Checkpoint import check_flag, set_flag
from inventory.Item import FixtureSpec

class Stoplight(FixtureSpec):

  def __init__(self) -> None:
    super().__init__()
    flag = check_flag("south_west_light")
    crosswalk = check_flag("south_west_crosswalk")
    self.state = flag if flag else "🔴"
    self.cross = crosswalk if crosswalk else "✋"

  def __str__(self) -> str:
    return f"{self.state} {self.cross}"

  def use(self) -> None:
    # Do not alter
    light = self.state
    crosswalk = random.choice(["✋","🚶"])
    # Do not alter

    #----------------------
    if crosswalk == "🚶":
      light = "🔴"
    elif crosswalk == "✋":
      light = "🟢"
    #----------------------
    
    # Do not alter
    self.state = light
    self.cross = crosswalk
    set_flag("south_west_light", self.state)
    set_flag("south_west_crosswalk", self.cross)
    # Do not alter

def main():
  stoplight = Stoplight()
  stoplight.use()
  print(stoplight)

if __name__ == "__main__":
  main()