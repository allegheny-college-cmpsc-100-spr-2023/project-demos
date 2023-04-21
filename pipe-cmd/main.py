import os

"""
    Run this using:
        . move "$(python main.py)"
"""

def main():
    return os.path.expanduser("~/.inv")

if __name__ == "__main__":
    loc = main()
    print(loc)