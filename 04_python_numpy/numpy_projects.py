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
 