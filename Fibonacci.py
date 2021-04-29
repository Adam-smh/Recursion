# Formula for sequence
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Try and While statements avoid breaking
while True:
    try:
        no_of_terms = int(input("Number of Fibonacci terms: "))
        if no_of_terms < 0:
            print("Must be a positive number... ")
            continue
    except ValueError:
        print("Not a number, Retry...")
        continue
    break

# Number of terms is printed according to the no_of_terms int
for i in range(no_of_terms):
    print(fibonacci(i))
