import sqlite3
import random
import matplotlib.pyplot as plt

# --- CONFIGURATION ---
DB_NAME = "population_MC.db" 
CITIES = [
    "Jacksonville", "Miami", "Tampa", "Orlando", "St. Petersburg",
    "Tallahassee", "Port St. Lucie", "Fort Lauderdale", "Cape Coral", "Hollywood"
]
START_YEAR = 2025
END_YEAR = 2045
INITIAL_POP_RANGE = (100000, 1000000)

# --- FUNCTIONS ---

def setup_database():
    """Creates the database and table."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    # Create table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS population (
            city TEXT,
            year INTEGER,
            population INTEGER
        )
    ''')
    # Clear existing data for re-run capability
    cursor.execute('DELETE FROM population')
    conn.commit()
    conn.close()
    print(f"Database {DB_NAME} and table 'population' initialized.")

def populate_and_simulate():
    """Inserts initial 2025 data and simulates 20 years of growth/decline."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    for city in CITIES:
        # Initial population for 2025
        current_pop = random.randint(INITIAL_POP_RANGE[0], INITIAL_POP_RANGE[1])
        cursor.execute('INSERT INTO population VALUES (?, ?, ?)', (city, START_YEAR, current_pop))
        
        # Simulate next 20 years
        for year in range(START_YEAR + 1, END_YEAR + 1):
            # Random growth rate between -2% and +5%
            growth_rate = random.uniform(-0.02, 0.05)
            current_pop = int(current_pop * (1 + growth_rate))
            cursor.execute('INSERT INTO population VALUES (?, ?, ?)', (city, year, current_pop))
            
    conn.commit()
    conn.close()
    print(f"Simulated data for 10 cities from {START_YEAR} to {END_YEAR} inserted.")

def visualize_city_population():
    """Allows user to select a city and displays population graph."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    
    print("\nAvailable Cities:")
    for i, city in enumerate(CITIES, 1):
        print(f"{i}. {city}")
        
    try:
        choice = int(input("\nSelect a city number to view growth: "))
        selected_city = CITIES[choice - 1]
        
        # Fetch data
        cursor.execute('''
            SELECT year, population FROM population 
            WHERE city = ? ORDER BY year
        ''', (selected_city,))
        data = cursor.fetchall()
        
        years = [row[0] for row in data]
        populations = [row[1] for row in data]
        
        # Plotting
        plt.figure(figsize=(10, 6))
        plt.plot(years, populations, marker='o', linestyle='-', color='b')
        plt.title(f'Population Projection for {selected_city} (2025-2045)')
        plt.xlabel('Year')
        plt.ylabel('Population')
        plt.grid(True)
        plt.tight_layout()
        plt.show()
        
    except (ValueError, IndexError):
        print("Invalid selection.")
    finally:
        conn.close()

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    setup_database()
    populate_and_simulate()
    visualize_city_population()
