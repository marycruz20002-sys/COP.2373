def display_remaining(tickets_left):
    """Function 1: Displays the remaining tickets."""
    print(f"Remaining tickets: {tickets_left}")

def sell_tickets():
    """Function 2: Manages the tickets selling logic."""
    total_tickets = 20
    buyers = 0    
    # Repeating loop until all stubs are sold
    while total_tickets > 0:
        display_remaining(total_tickets)
        try:
            # Input number of stubs
            requested = int(input("Select amount of tickets to purchase (1-4): "))
            # Validation using if statement for incorrect number of tickets
            if requested < 1 or requested > 4:
                print("Invalid amount. You can buy 1-4 tickets.")
                continue
            # Validation using if statement for insufficient tickets remaining
            if requested > total_tickets:
                print(f"Not enough tickets. Only {total_tickets} left.")
                continue
                
            # Update ticket count (accumulator)
            total_tickets -= requested
            buyers += 1 # Accumulator for buyers
            
            # Output
            print(f"Sold {requested} ticket(s).")
            
        except ValueError:
            print("Invalid input. Please enter a number.")

    print(f"All tickets sold! Total buyers: {buyers}")

# Run the program
sell_tickets()
