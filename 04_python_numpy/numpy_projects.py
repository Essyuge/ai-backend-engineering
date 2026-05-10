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

   
# ============================================================================
# PROJECT 3: STUDENT GRADES ANALYSIS
# ============================================================================
 
def project_3_grades():
    print_header("PROJECT 3: STUDENT GRADES ANALYSIS")
    
    print_code_section("3.1 - Create grade dataset")
    print("Use case: Analyze student performance across multiple exams")
    print()
    
    # Student scores: 5 students, 4 exams each
    grades = np.array([
        [85, 88, 90, 92],  # Alice
        [78, 80, 82, 85],  # Bob
        [92, 94, 96, 98],  # Charlie
        [65, 68, 70, 72],  # David
        [88, 85, 87, 90],  # Emma
    ])
    
    students = np.array(['Alice', 'Bob', 'Charlie', 'David', 'Emma'])
    exams = ['Exam 1', 'Exam 2', 'Exam 3', 'Exam 4']
    
    print(f"Grades shape: {grades.shape} (5 students × 4 exams)")
    print("Grades:\n", grades)
    
    separator()
    print_code_section("3.2 - Performance analysis")
    
    # Each student's average
    student_avg = grades.mean(axis=1)
    print("Student averages:")
    for name, avg in zip(students, student_avg):
        status = "✓ Good" if avg >= 75 else "✗ Needs help"
        print(f"  {name:10s}: {avg:6.2f}  {status}")
    
    # Each exam's difficulty
    exam_avg = grades.mean(axis=0)
    print(f"\nExam difficulty (average scores):")
    for exam, avg in zip(exams, exam_avg):
        print(f"  {exam}: {avg:.2f}")
    
    separator()
    print_code_section("3.3 - Identify top/bottom performers")
    
    # Best student
    best_idx = student_avg.argmax()
    best_student = students[best_idx]
    print(f"Best student: {best_student} ({student_avg[best_idx]:.2f})")
    
    # Worst student
    worst_idx = student_avg.argmin()
    worst_student = students[worst_idx]
    print(f"Student needing help: {worst_student} ({student_avg[worst_idx]:.2f})")
    
    # Struggling students (average < 75)
    struggling = students[student_avg < 75]
    print(f"Students below 75: {struggling}")
    
    # Top performers
    top_students = students[student_avg >= 90]
    print(f"Outstanding students (90+): {top_students}")
    
    separator()
    print_code_section("3.4 - Grade normalization")
    
    # Normalize grades to 0-1 scale
    min_grade = grades.min()
    max_grade = grades.max()
    normalized = (grades - min_grade) / (max_grade - min_grade)
    print(f"Normalized grades (0-1 scale):")
    print(normalized)
    
    # Scale to 0-100
    scaled = normalized * 100
    print(f"\nScaled to 0-100:")
    print(scaled)
    
    separator()
    print_code_section("3.5 - Pass/Fail statistics")
    
    passed = (student_avg >= 70).sum()
    failed = (student_avg < 70).sum()
    print(f"Passed: {passed} students")
    print(f"Failed: {failed} students")
    print(f"Pass rate: {passed/len(students)*100:.1f}%")
    
    # Grade distribution
    A = (student_avg >= 90).sum()
    B = ((student_avg >= 80) & (student_avg < 90)).sum()
    C = ((student_avg >= 70) & (student_avg < 80)).sum()
    F = (student_avg < 70).sum()
    
    print(f"\nGrade distribution:")
    print(f"  A (90+): {A} students")
    print(f"  B (80-89): {B} students")
    print(f"  C (70-79): {C} students")
    print(f"  F (<70): {F} students")
    
    separator()

 # ============================================================================
# PROJECT 4: SALES DATA ANALYSIS
# ============================================================================
 
def project_4_sales():
    print_header("PROJECT 4: SALES DATA ANALYSIS")
    
    print_code_section("4.1 - Create sales dataset")
    print("Use case: Analyze multi-store, multi-quarter sales")
    print()
    
    # Sales data: 3 stores, 4 quarters
    sales = np.array([
        [50000, 55000, 60000, 65000],   # NYC Store
        [40000, 42000, 45000, 48000],   # LA Store
        [60000, 62000, 65000, 70000],   # Chicago Store
    ])
    
    stores = np.array(['NYC', 'LA', 'Chicago'])
    quarters = np.array(['Q1', 'Q2', 'Q3', 'Q4'])
    
    print(f"Sales shape: {sales.shape} (3 stores × 4 quarters)")
    print("Sales data (in dollars):")
    print(sales)
    
    separator()
    print_code_section("4.2 - Store performance")
    
    # Total sales per store
    store_totals = sales.sum(axis=1)
    print("Total annual sales per store:")
    for store, total in zip(stores, store_totals):
        print(f"  {store:10s}: ${total:,}")
    
    # Average sales per store
    store_avg = sales.mean(axis=1)
    print("\nAverage quarterly sales per store:")
    for store, avg in zip(stores, store_avg):
        print(f"  {store:10s}: ${avg:,.0f}")
    
    # Best and worst store
    best_store = stores[store_totals.argmax()]
    worst_store = stores[store_totals.argmin()]
    print(f"\nBest store: {best_store}")
    print(f"Worst store: {worst_store}")
    
    separator()
    print_code_section("4.3 - Quarterly performance")
    
    # Quarterly totals
    quarterly_totals = sales.sum(axis=0)
    print("Total sales per quarter:")
    for quarter, total in zip(quarters, quarterly_totals):
        print(f"  {quarter}: ${total:,}")
    
    # Best quarter
    best_quarter = quarters[quarterly_totals.argmax()]
    print(f"\nBest quarter: {best_quarter}")
    
    separator()
    print_code_section("4.4 - Growth analysis")
    
    # Growth rate (Q4 vs Q1)
    growth = ((sales[:, 3] - sales[:, 0]) / sales[:, 0] * 100)
    print("Growth rates (Q1 to Q4):")
    for store, rate in zip(stores, growth):
        direction = "↑" if rate > 0 else "↓"
        print(f"  {store:10s}: {direction} {rate:+.1f}%")
    
    separator()
    print_code_section("4.5 - Store rankings")
    
    # Rank stores by total sales
    rank_indices = np.argsort(store_totals)[::-1]  # Descending order
    print("Store rankings by total sales:")
    for i, idx in enumerate(rank_indices, 1):
        print(f"  {i}. {stores[idx]:10s}: ${store_totals[idx]:,}")
    
    separator()

 
# ============================================================================
# PROJECT 5: STATISTICS & DISTRIBUTIONS
# ============================================================================
 
def project_5_statistics():
    print_header("PROJECT 5: STATISTICS & DISTRIBUTIONS")
    
    print_code_section("5.1 - Generate random data")
    print("Use case: Analyze test scores with statistical methods")
    print()
    
    # Generate random test scores (100 students)
    np.random.seed(42)  # Reproducible results
    scores = np.random.normal(75, 15, 100)  # Mean 75, std 15
    scores = np.clip(scores, 0, 100)  # Keep between 0-100
    
    print(f"Generated {len(scores)} student test scores")
    print(f"First 10 scores: {scores[:10]}")
    
    separator()
    print_code_section("5.2 - Descriptive statistics")
    
    print(f"Mean (average): {scores.mean():.2f}")
    print(f"Median (middle value): {np.median(scores):.2f}")
    print(f"Mode (most frequent): ~{np.round(np.median(scores), 0):.0f}")
    print(f"Std Dev (spread): {scores.std():.2f}")
    print(f"Variance: {scores.var():.2f}")
    print(f"Min: {scores.min():.2f}")
    print(f"Max: {scores.max():.2f}")
    print(f"Range: {scores.max() - scores.min():.2f}")
    
    separator()
    print_code_section("5.3 - Percentiles")
    
    p25, p50, p75 = np.percentile(scores, [25, 50, 75])
    print(f"25th percentile (Q1): {p25:.2f}")
    print(f"50th percentile (Median): {p50:.2f}")
    print(f"75th percentile (Q3): {p75:.2f}")
    print(f"IQR (Q3-Q1): {p75-p25:.2f}")
    
    # Top performers
    p90, p95, p99 = np.percentile(scores, [90, 95, 99])
    print(f"\nTop performers:")
    print(f"  Top 10% (90th): {p90:.2f}")
    print(f"  Top 5% (95th): {p95:.2f}")
    print(f"  Top 1% (99th): {p99:.2f}")
    
    separator()
    print_code_section("5.4 - Grade distribution")
    
    A = (scores >= 90).sum()
    B = ((scores >= 80) & (scores < 90)).sum()
    C = ((scores >= 70) & (scores < 80)).sum()
    D = ((scores >= 60) & (scores < 70)).sum()
    F = (scores < 60).sum()
    
    total = len(scores)
    print(f"A (90-100): {A:3d} students ({A/total*100:5.1f}%)")
    print(f"B (80-89):  {B:3d} students ({B/total*100:5.1f}%)")
    print(f"C (70-79):  {C:3d} students ({C/total*100:5.1f}%)")
    print(f"D (60-69):  {D:3d} students ({D/total*100:5.1f}%)")
    print(f"F (<60):    {F:3d} students ({F/total*100:5.1f}%)")
    
    separator()
    print_code_section("5.5 - Outliers")
    
    # Outliers (beyond 2 std dev)
    mean = scores.mean()
    std = scores.std()
    outlier_threshold = 2
    outliers = np.abs(scores - mean) > outlier_threshold * std
    outlier_count = outliers.sum()
    
    print(f"Outliers (>{outlier_threshold} std dev): {outlier_count} students")
    if outlier_count > 0:
        outlier_scores = scores[outliers]
        print(f"Outlier scores: {np.sort(outlier_scores)}")
    
    separator() 