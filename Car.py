import os
import sys
import shutil
import narrator

from importlib import import_module
from narrator.Checkpoint import check_flag, set_flag
from inventory.Item import FixtureSpec

class Car(FixtureSpec):

    def __init__(self):
        super().__init__()
        #self. n = narrator.Narrator()
        self.curr_dir = check_flag("cwd")

    def __get_light(self, direction) -> any:
        stoplight = import_module(
            f"{direction}.Stoplight"
        )
        return stoplight.Stoplight()

    def use(self, direction: str = "north") -> None:
        # Do not alter
        move_to = None
        stoplight = self.__get_light(direction)
        stoplight.use()
        signal = stoplight.state
        print(f"light: {signal}")
        # Do not alter

        #------------------------
        """
        TODO: Create stoplight functionality using directions, variables, and
              guidance from the README. This vehicle uses:

          * signal
          * move_to
        """
        #------------------------

        # Do not alter
        if move_to:
            shutil.move(
                f"{os.getcwd()}/Car.py",
                os.path.join(
                    self.curr_dir,
                    move_to
                )
            )
        # Do not alter

def main():
    direction = input("Direction: ")

    cwd = check_flag("cwd")

    sys.path.append(cwd)

    obj = Car()
    obj.use(direction)

    # Keep track of where this thing has gone
    os.replace(".car",f"{cwd}/.car")

if __name__ == "__main__":
    main()