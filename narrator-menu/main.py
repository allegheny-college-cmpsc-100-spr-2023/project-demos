import json
import narrator

def main():
    use = narrator.YesNoQuestion({
        "question": "Use the machine? ",
        "outcomes": [True, False]
    })
    
    response = use.ask()

    if response:
        # Load the items from an inventory file
        with open(".inventory", "r") as fh:
            items = json.load(fh)
        stock = []
        for item in items:
            print(item)
            item_no = len(stock) + 1
            stock.append(
                {"choice": f"{item_no} {item} ({items[item]})", "outcome": item_no}
            )
        selection = narrator.Question({
            "question": "\nChoose a thing:\n",
            "responses": stock
        })
        response = selection.ask()
        print(response)

if __name__ == "__main__":
    main()
