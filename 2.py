K = set(range(1, 51))
M = set()
for denominator in K:
    numerator = denominator - 1
    M.add(numerator)
print("Максимальні чисельники для правильних дробів:")
print(sorted(M))
