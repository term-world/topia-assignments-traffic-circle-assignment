import narrator

from datetime import datetime

from narrator.Checkpoint import check_flag, set_flag
from inventory.Item import FixtureSpec


class Stoplight(FixtureSpec):
    def __init__(self) -> None:
        super().__init__()
        flag = check_flag("southeast_light")
        light_time = check_flag("southeast_time")
        walk_flag = check_flag("southeast_walk")
        self.crosswalk = walk_flag if walk_flag else "✋"
        self.state = flag if flag else "🔴"
        self.timing = light_time if light_time else 0

    def __time_now(self) -> str:
        now = datetime.now().timestamp()
        return now

    def __timing(self) -> bool:
        now = float(self.__time_now())
        then = float(self.timing)
        difference = now - then
        return difference

    def __str__(self) -> str:
        return f"{self.state} {self.crosswalk}"

    def use(self) -> None:
        # Do not alter
        light = self.state
        crosswalk = self.crosswalk
        countdown = int(self.__timing())
        # Do not alter

        # ----------------------
        """
        TODO: Create stoplight functionality using directions, variables, and
              guidance from the README. This light uses:

          * light
          * crosswalk
          * countdown
        """
        # ----------------------

        # Do not alter
        self.state = light
        self.crosswalk = crosswalk
        set_flag("southeast_light", self.state)
        if countdown > 15:
            set_flag("southeast_time", self.__time_now())
        set_flag("southeast_walk", crosswalk)
        # Do not alter


def main():
    stoplight = Stoplight()
    stoplight.use()
    print(stoplight)


if __name__ == "__main__":
    main()
