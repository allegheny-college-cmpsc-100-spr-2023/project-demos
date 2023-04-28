import os
import json

def main():
    route = {}
    cwd = os.getcwd()
    while True:
        direction = input("Direction: ")
        if not direction:
            break
        route[direction] = f"{cwd}/{direction}"
    with open("track/.track.json", "w") as fh:
        json.dump(route, fh)

if __name__ == "__main__":
    main()