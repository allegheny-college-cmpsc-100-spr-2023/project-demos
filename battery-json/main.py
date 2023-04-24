import os
import json
import resources

def main():
    batt = {
        "biomass": 10
    }
    path = os.path.dirname(resources.__file__)
    with open(f"{path}/worldbattery.json", "w") as fh:
        json.dump(batt, fh)

if __name__ == "__main__":
    main()