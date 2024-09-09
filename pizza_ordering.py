def display_menu():
    menu = {
        1: "Margherita",
        2: "Pepperoni",
        3: "Hawaiian",
        4: "Vegetarian"
    }
    
    print("\nPizza Menu:")
    for number, pizza in menu.items():
        print(f"{number}. {pizza}")

def get_order():
    try:
        order_number = int(input("\nEnter the number of the pizza you'd like to order: "))
        return order_number
    except ValueError:
        print("Error: Please enter a valid number.")
        return None

def process_order(order_number):
    # This function should process the order and calculate the price
    prices = {
        1: 8.99,
        2: 9.99,
        3: 10.99,
        4: 7.99
    }

    if order_number not in prices:
        print("Sorry, we don't have that pizza on the menu.")
        return None
    
    pizza_price = prices[order_number]  # Runtime error: 'order_number' might be None
    print(f"Great choice! That will be ${pizza_price}.")
    return pizza_price

def finalize_order(price):
    if price is not None:
        try:
            quantity = int(input("\nHow many pizzas would you like to order? "))
            total = price * quantity
            print(f"\nYour total is: ${total}")
        except ValueError:
            print("Error: Please enter a valid number for the quantity.")
    else:
        print("No order to finalize.")

def main():
    print("Welcome to Pizza Planet!")
    display_menu()
    
    order_number = get_order()
    pizza_price = process_order(order_number)
    finalize_order(pizza_price)

if __name__ == "__main__":
    main()
