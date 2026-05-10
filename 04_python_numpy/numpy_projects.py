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


 