import cookies

def main():
    tracking = cookies.fetch("Test")
    if not tracking:
        Cookie(name = "")
        

if __name__ == "__main__":
    main()