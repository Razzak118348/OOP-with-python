sq = lambda x: x ** 2
print(sq(3))


# Example: Check if a number is positive, negative, or zero
n = lambda x: "Positive" if x > 0 else "Negative" if x < 0 else "Zero"

print(n(5))
print(n(-3))
print(n(0))


s1 = 'GeeksforGeeks'

s2 = lambda variable: variable.upper()
print(s2(s1))
