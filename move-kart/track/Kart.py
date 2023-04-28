import json
import shutil
import subprocess

class Kart:

    def __init__(self):
        with open(".track.json") as fh:
            self.route = json.load(fh)

    def __move(self, direction:str = ""):
        shutil.move(__file__, self.route[direction])

    def turn(self, direction: str = "left") -> None:
        subprocess.call(
            f' -c "cd {direction} && exec $SHELL"', 
            shell = True
        )
        self.__move(direction)

def main():
    kart = Kart()
    kart.turn()

if __name__ == "__main__":
    main()