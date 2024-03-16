class SquareGenerator:
    def generate_squares(self, start, end):
        return [x**2 for x in range(start, end+1)]

generator = SquareGenerator()
start = 1
end = 10
squares = generator.generate_squares(start, end)
print(squares)