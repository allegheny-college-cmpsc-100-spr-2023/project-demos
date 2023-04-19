import narrator

def main():
    use = narrator.YesNoQuestion({
        "question": "Use the machine? ",
        "outcomes": [True, False]
    })
    
    response = use.ask()

    if response:
        selection = narrator.Question({
            "question": "\nChoose a thing:\n",
            "responses": [
                {"choice": "1 Soda ", "outcome": 1},
                {"choice": "2 Beet Juice ", "outcome": 2},
                {"choice": "3 Super Greens ", "outcome": 3},
                {"choice": "4 Carrot Juice ", "outcome": 4},
                {"choice": "5 Apple Juice", "outcome": 5}
            ]
        })
        response = selection.ask()
        print(response)

if __name__ == "__main__":
    main()
