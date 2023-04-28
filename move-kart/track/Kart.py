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
        self.__move(direction = direction)
        subprocess.call(
            f'sh -c "cd {self.route[direction]} && exec $SHELL"', 
            shell = True
        )

def main():
    kart = Kart()
    turn = input("Direction [left/right]: ")
    kart.turn(direction = turn)

if __name__ == "__main__":
    main()