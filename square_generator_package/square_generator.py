class SquareGenerator:
    def generate_squares(self, start, end):
        if end < start:
            return []
        return [x**2 for x in range(start, end + 1)]

class CubicGenerator(SquareGenerator):
    def generate_squares(self, start, end):
        if end < start:
            raise ValueError("End of range must be greater than or equal to start.")
        return [x**2 for x in range(start, end + 1)]

# Example usage of the CubicGenerator subclass
cubic_gen = CubicGenerator()

# Generate squares from 1 to 5
squares_list = cubic_gen.generate_squares(1, 5)
print(squares_list)