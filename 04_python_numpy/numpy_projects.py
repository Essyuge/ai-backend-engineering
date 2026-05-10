import numpy as np
import sys


# Color codes for pretty output
GREEN = '\033[92m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'
BOLD = '\033[1m'

print(GREEN + 'Hello, welcome to the NumPy projects!' + RESET)
print('Hello there! Welcome to the NumPy projects!')


def print_header(title):
    """Print a colored section header"""
    print(f"\n{BOLD}{BLUE}{'='*60}{RESET}")
    print(f"{BOLD}{BLUE}▶ {title}{RESET}")
    print(f"{BOLD}{BLUE}{'='*60}{RESET}\n")
 
def print_code_section(code_title):
    """Print subsection title"""
    print(f"\n{YELLOW}→ {code_title}{RESET}")
    print(f"{YELLOW}{'-'*50}{RESET}")
 
def separator():
    """Print a separator line"""
    print(f"\n{BLUE}{'-'*60}{RESET}\n")

def print_result(description, result):
    """Print the result of a code block with description"""
    print(f"{GREEN}{description}:{RESET} {result}")

# ============================================================================
# PROJECT 1: STOCK PORTFOLIO ANALYSIS
# ============================================================================
 
def project_1_stocks():
    print_header("PROJECT 1: STOCK PORTFOLIO ANALYSIS")
    
    print_code_section("1.1 - Create stock data arrays")
    print("Use case: Track stock prices and calculate portfolio value")
    print()
    
    # Create arrays (Stock prices for 5 days)
    prices = np.array([100, 105, 102, 108, 110])
    print(f'stock prices: {prices}')
    
    
    # Create array with range (Days 0-4)
    days = np.arange(5)
    print(f"Days: {days}")
    
    # Create array of zeros
    portfolio = np.zeros(5)
    print(f"Empty portfolio (all zeros): {portfolio}")
    
    # Create array with specific value
    # Assuming we bought 10 shares each day, we can create an array of quantities
    # Alternatively, if we want to track the number of shares bought each day, we could create an array with different values for each day.
    #  For simplicity, let's assume we bought 10 shares each day.
    # In a real scenario, we might have different quantities for each day, which could be represented as an array like: quantities = np.array([10, 15, 12, 20, 18])
    # For this example, we'll keep it simple and use the same quantity for each day.
    quantities = np.full(5, 10)  # 10 shares of each stock each day
    print(f"Quantities per day: {quantities}")


    separator()
    print_code_section("1.2 - Calculate portfolio value")
    
    # Basic math operations
    total_value = prices * quantities
    print(f"Total value per day: {total_value}")
    print(f"Total portfolio value: ${total_value.sum()}")
    print(f"Average stock price: ${prices.mean():.2f}")
    print(f"Price range: ${prices.max() - prices.min()}")
    print(f"Highest price: ${prices.max()} (Day {prices.argmax()})")
    print(f"Lowest price: ${prices.min()} (Day {prices.argmin()})")
    
    separator()
    print_code_section("1.3 - Profit/Loss analysis")
    
    # Calculate daily changes
    price_changes = np.diff(prices)  # Difference between consecutive days
    print(f"Daily price changes: {price_changes}")
    
    # Cumulative returns
    returns = (prices - prices[0]) / prices[0] * 100
    print(f"Daily returns (% from Day 1): {returns}")
    print(f"Total return: {returns[-1]:.2f}%")
    
    separator()
 
 
# ============================================================================
# PROJECT 2: WEATHER DATA ANALYSIS
# ============================================================================
 
def project_2_weather():
    print_header("PROJECT 2: WEATHER & TEMPERATURE ANALYSIS")
    
    print_code_section("2.1 - Create temperature dataset")
    print("Use case: Analyze multi-dimensional weather data")
    print()
    
    # Weather data: 7 days of temp readings (4 readings per day)
    temperatures = np.array([
        [22, 23, 24, 23],  # Day 1 (morning, noon, afternoon, evening)
        [21, 22, 23, 22],  # Day 2
        [20, 21, 22, 21],  # Day 3
        [19, 20, 21, 20],  # Day 4
        [18, 19, 20, 19],  # Day 5
        [17, 18, 19, 18],  # Day 6
        [16, 17, 18, 17],  # Day 7
    ])
    
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    times = ['6AM', '12PM', '6PM', '12AM']
    
    print(f"Dataset shape: {temperatures.shape} (7 days × 4 readings)")
    print(f"Temperature data:\n{temperatures}\n")
    
    separator()
    print_code_section("2.2 - Analyze temperatures")
    
    # Daily average temperature
    daily_avg = temperatures.mean(axis=1)
    print("Daily averages:")
    for day, avg in zip(days, daily_avg):
        print(f"  {day}: {avg:.1f}°C")
    
    # Hourly average across all days
    hourly_avg = temperatures.mean(axis=0)
    print(f"\nHourly averages: {hourly_avg}")
    for time, avg in zip(times, hourly_avg):
        print(f"  {time}: {avg:.1f}°C")
    
    # Hottest and coldest
    print(f"\nMax temperature: {temperatures.max()}°C (Day {temperatures.argmax() // 4 + 1})")
    print(f"Min temperature: {temperatures.min()}°C (Day {temperatures.argmin() // 4 + 1})")
    
    separator()
    print_code_section("2.3 - Filter and analyze conditions")
    
    # Days above 20 degrees
    warm_days = (daily_avg > 20).sum()
    print(f"Days warmer than 20°C: {warm_days} days")
    
    # Cold days
    cold_days = (daily_avg < 18).sum()
    print(f"Days colder than 18°C: {cold_days} days")
    
    # Get indices of warm days
    warm_indices = np.where(daily_avg > 20)[0]
    print(f"Warm days (indices): {warm_indices}")
    print(f"Warm days (names): {[days[i] for i in warm_indices]}")
    
    # Get data only for warm days
    warm_data = temperatures[daily_avg > 20]
    print(f"Warm days data shape: {warm_data.shape}")
    
    separator()