import narrator

from datetime import datetime, timedelta
from narrator.Checkpoint import check_flag, set_flag
from inventory.Item import FixtureSpec

class Stoplight(FixtureSpec):

    def __init__(self) -> None:
        super().__init__()
        light_flag = check_flag("east_light")
        light_time = check_flag("east_turn")
        self.state = light_flag if light_flag else "🔴"
        self.timing = light_time if light_time else 0

    def __str__(self) -> str:
        self.state += "\n➡️" if self.turn_signal else ""
        return self.state

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
        turn = not self.__timing()
        hold = not self.timing == "0"
        # Do not alter

        #----------------------
        if light == "🔴":
            light = "🟢"
            turn = True
        elif light == "🟡":
            light = "🔴"
        if turn:
            light == "🟢"
        elif light == "🟢" and not turn:
            pass
        if light == "🟢" and not hold and not turn:
            light = "🟡"
        #----------------------
    
        # Do not alter
        self.state = light
        self.turn_signal = turn
        set_flag("east_light", self.state)
        if turn and self.__timing():
            set_flag("east_turn", self.__time_now())
        elif light == "🟢" and not turn: 
            set_flag("east_turn", "0")
        # Do not alter

def main():
    stoplight = Stoplight()
    stoplight.use()
    print(stoplight)

if __name__ == "__main__":
    main()