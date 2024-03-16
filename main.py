import math

class SquareGenerator:
    def generate_squares(self, start, end):
        """
        Generates a list of squares for numbers in the given range [start, end].
        """
        return [x**2 for x in range(start, end + 1)]

# Create an instance of the SquareGenerator class
square_gen = SquareGenerator()

# Generate squares from 1 to 10
squares_list = square_gen.generate_squares(1, 10)

# Calculate the square root of each number in the squares list
square_roots = [math.sqrt(number) for number in squares_list]

# Print the list of squares
print("Squares list:", squares_list)

# Print the list of square roots
print("Square roots list:", square_roots)