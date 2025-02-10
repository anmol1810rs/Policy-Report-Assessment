import unittest
from best_threshold import compute_best_threshold
from tests import TestBestThreshold  # Import test class

def run_tests():
    """Run all unit tests and return True if they pass, False otherwise."""
    print("\nRunning unit tests...\n")
    test_suite = unittest.TestLoader().loadTestsFromTestCase(TestBestThreshold)
    test_result = unittest.TextTestRunner().run(test_suite)
    
    if test_result.wasSuccessful():
        print("All tests passed!\n")
        return True
    else:
        print("Some tests failed. Fix issues before proceeding.\n")
        return False

def main():
    """
    Runs the threshold computation after tests pass.
    """
    if not run_tests():
        return
    
    disease_risk_data = [
        {"threshold": 0.1, "TP": 120, "FP": 50, "TN": 830, "FN": 10},
        {"threshold": 0.2, "TP": 115, "FP": 40, "TN": 840, "FN": 15},
        {"threshold": 0.3, "TP": 110, "FP": 30, "TN": 850, "FN": 20},
        {"threshold": 0.4, "TP": 105, "FP": 20, "TN": 860, "FN": 25},
        {"threshold": 0.5, "TP": 100, "FP": 15, "TN": 865, "FN": 30},
        {"threshold": 0.6, "TP": 95, "FP": 10, "TN": 870, "FN": 35},
        {"threshold": 0.7, "TP": 90, "FP": 5, "TN": 875, "FN": 40},
        {"threshold": 0.8, "TP": 85, "FP": 3, "TN": 877, "FN": 45},
        {"threshold": 0.9, "TP": 80, "FP": 1, "TN": 879, "FN": 50}
    ]

    best_threshold_disease = compute_best_threshold(disease_risk_data)
    print(f"Best threshold for disease risk prediction: {best_threshold_disease}\n")

if __name__ == "__main__":
    main()
