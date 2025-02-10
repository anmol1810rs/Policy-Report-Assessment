import unittest
from best_threshold import compute_best_threshold

class TestBestThreshold(unittest.TestCase):
    
    def test_correct_threshold_selection(self):
        """Test that the function returns the correct best threshold with recall >= 0.9"""
        disease_risk_data = [
            {"threshold": 0.1, "TP": 120, "FP": 50, "TN": 830, "FN": 10},  # Recall = 0.923
            {"threshold": 0.2, "TP": 115, "FP": 40, "TN": 840, "FN": 15},  # Recall = 0.884
            {"threshold": 0.3, "TP": 110, "FP": 30, "TN": 850, "FN": 20}   # Recall = 0.846
        ]
        self.assertEqual(compute_best_threshold(disease_risk_data), 0.1)

    def test_no_valid_threshold(self):
        """Test that the function returns the expected message when no threshold meets recall >= 0.9"""
        data = [
            {"threshold": 0.1, "TP": 50, "FP": 50, "TN": 900, "FN": 100},  # Recall < 0.9
            {"threshold": 0.2, "TP": 40, "FP": 30, "TN": 920, "FN": 110}   # Recall < 0.9
        ]
        self.assertEqual(compute_best_threshold(data), "No threshold meets recall >= 0.9")

    def test_only_one_threshold_meets_recall(self):
        """Test when only one threshold meets recall criteria, it selects that one"""
        data = [
            {"threshold": 0.1, "TP": 50, "FP": 20, "TN": 880, "FN": 50},  # Recall = 0.5
            {"threshold": 0.2, "TP": 95, "FP": 40, "TN": 850, "FN": 5}    # Recall = 0.95
        ]
        self.assertEqual(compute_best_threshold(data), 0.2)

if __name__ == "__main__":
    unittest.main()
