def my_function(x):
    if x <= 0:  # Corrected base case
        return 1  # Or handle negative inputs appropriately
    else:
        return x / my_function(x - 1) 