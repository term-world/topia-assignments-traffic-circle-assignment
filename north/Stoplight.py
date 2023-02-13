import narrator

from narrator.Checkpoint import check_flag, set_flag
from inventory.Item import FixtureSpec


class Stoplight(FixtureSpec):
    def __init__(self) -> None:
        super().__init__()
        flag = check_flag("north_light")
        self.state = flag if flag else "🔴"

    def __str__(self) -> str:
        return self.state

    def use(self) -> None:
        # Do not alter
        light = self.state
        # Do not alter

        # ----------------------
        """
        TODO: Create stoplight functionality using directions, variables, and
              guidance from the README. This light uses:

          * light
        """
        # ----------------------

        # Do not alter
        self.state = light
        set_flag("north_light", self.state)
        # Do not alter


def main():
    stoplight = Stoplight()
    stoplight.use()
    print(stoplight)


if __name__ == "__main__":
    main()
