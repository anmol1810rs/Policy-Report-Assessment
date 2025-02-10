def compute_best_threshold(threshold_values):
    """
    Finds the best threshold that yields recall >= 0.9 based on the highest F1-score.
    """
    best_threshold = None
    best_f1_score = 0  

    for entry in threshold_values:
        threshold, tp, fp, tn, fn = entry["threshold"], entry["TP"], entry["FP"], entry["TN"], entry["FN"] 
        
        # Compute recall safely
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0
        
        if recall >= 0.9:
            # Compute precision safely
            precision = tp / (tp + fp) if (tp + fp) > 0 else 0
            
            # Compute F1-score safely
            f1_score = (2 * precision * recall) / (precision + recall) if (precision + recall) > 0 else 0

            # Track best threshold based on highest F1-score
            if f1_score > best_f1_score:
                best_threshold = threshold
                best_f1_score = f1_score
    
    return best_threshold if best_threshold is not None else "No threshold meets recall >= 0.9"
