import narrator

from datetime import datetime, timedelta
from narrator.Checkpoint import check_flag, set_flag
from inventory.Item import FixtureSpec

class Stoplight(FixtureSpec):

    def __init__(self) -> None:
        super().__init__()
        light_flag = check_flag("west_light")
        light_time = check_flag("west_time")
        self.state = light_flag if light_flag else "🔴"
        self.timing = light_time if light_time else "0"

    def __str__(self) -> str:
        return f"{self.state}"

    def __time_now(self) -> str:
        now = datetime.now().timestamp()
        return now

    def __timing(self) -> bool:
        now = float(self.__time_now())
        then = float(self.timing)
        difference = now - then
        return difference > 5
 
    def use(self) -> None:
        # Do not alter
        light = self.state
        timeout = self.__timing()
        # Do not alter

        #----------------------
        """
        TODO: Create stoplight functionality using directions, variables, and
                guidance from the README. This light uses:

                * light
                * timeout
        """
        #----------------------
        
        # Do not alter
        self.state = light
        set_flag("west_light", self.state)
        if self.__timing():
            set_flag("west_time", self.__time_now())
        # Do not alter

def main():
    stoplight = Stoplight()
    stoplight.use()
    print(stoplight)

if __name__ == "__main__":
    main()