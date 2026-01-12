def recursive_search(logs, target_id, index=0):
    """
    Recursively searches through access logs for a specific User ID.
    Demonstrates functional programming skills required by HENNGE.
    """
    if index >= len(logs):
        return False
    if logs[index]['user_id'] == target_id:
        return True
    return recursive_search(logs, target_id, index + 1)

def recursive_sum_scores(scores, index=0):
    """Recursively calculates risk scores without loops."""
    if index >= len(scores):
        return 0
    return scores[index] + recursive_sum_scores(scores, index + 1)