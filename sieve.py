def primes(limit):
    all_numbers = [j for j in range(2, limit + 1)]

    for j in range(2, limit):
        if j in all_numbers:
            primes.append(j)
        for k in range(j + j, limit + 1, j):
            if k in all_numbers:
                all_numbers.remove(k)

    return all_numbers
