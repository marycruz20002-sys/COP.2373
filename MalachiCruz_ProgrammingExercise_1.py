def display_remaining(stubs_left):
    """Function 1: Displays the remaining stubs."""
    print(f"Remaining stubs: {stubs_left}")

def sell_stubs():
    """Function 2: Manages the stubs selling logic."""
    total_stubs = 10
    buyers = 0    
    # Repeating loop until all stubs are sold
    while total_stubs > 0:
        display_remaining(total_stubs)
        try:
            # Input number of stubs
            requested = int(input("How many stubs would you like to purchase? (1-4): "))
            # Validation using if statement for incorrect number of tickets
            if requested < 1 or requested > 4:
                print("Invalid amount. You can buy 1-4 stubs.")
                continue
            # Validation using if statement for insufficient stubs remaining
            if requested > total_stubs:
                print(f"Not enough tickets. Only {total_stubs} left.")
                continue
                
            # Update ticket count (accumulator)
            total_stubs -= requested
            buyers += 1 # Accumulator for buyers
            
            # Output
            print(f"Sold {requested} stub(s).")
            
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"All stubs sold! Total buyers: {buyers}")

# Run the program
sell_stubs()
