import numpy as np

def calculate_exam_stats(data):
    """Calculates and prints statistics for each individual exam (columns)."""
    num_exams = data.shape[1]
    print("--- Individual Exam Statistics ---")
    for i in range(num_exams):
        exam_col = data[:, i]
        passed = np.sum(exam_col >= 60)
        failed = len(exam_col) - passed
        
        print(f"Exam {i+1}:")
        print(f"  Mean: {np.mean(exam_col):.2f}")
        print(f"  Median: {np.median(exam_col)}")
        print(f"  Std Dev: {np.std(exam_col):.2f}")
        print(f"  Min/Max: {np.min(exam_col)} / {np.max(exam_col)}")
        print(f"  Passed: {passed}, Failed: {failed}")

def calculate_overall_stats(data):
    """Calculates and prints statistics for the entire dataset combined."""
    print("\n--- Overall Dataset Statistics ---")
    print(f"Overall Mean: {np.mean(data):.2f}")
    print(f"Overall Median: {np.median(data)}")
    print(f"Overall Std Dev: {np.std(data):.2f}")
    print(f"Overall Min: {np.min(data)}")
    print(f"Overall Max: {np.max(data)}")
    
    # Calculate overall pass percentage
    total_grades = data.size
    total_passed = np.sum(data >= 60)
    pass_percentage = (total_passed / total_grades) * 100
    print(f"Overall Pass Percentage: {pass_percentage:.2f}%")

try:
    dataset = np.genfromtxt('grades.csv', delimiter=',', skip_header=1)
    
    # 2. Print first few rows to verify structure
    print("Dataset Preview (First 5 Students):")
    print(dataset[:5])
    print("-" * 30)

    # 3. Call functions for analysis
    calculate_exam_stats(dataset)
    calculate_overall_stats(dataset)

except Exception as e:
    print(f"Error loading CSV: {e}")
