from module import enter_club

# Test case 1: Valid name, age, and ID
enter_club("John", 20, True)  # Expected output: "Welcome to the club"

# Test case 2: Invalid name
enter_club("David", 25, True)  # Expected output: "David are not allowed in the club"

# Test case 3: Missing ID
enter_club("Alice", 22, False)  # Expected output: "You need ID"

# Test case 4: Invalid age
enter_club("Bob", 17, True)  # Expected output: "You need ID"

# Test case 5: Invalid name, age, and ID
enter_club("David", 17, False)  # Expected output: "David are not allowed in the club"

