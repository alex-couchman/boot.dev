def get_num_guesses(length):
    total = 0
    for i in range(length):
        total += 26 ** (i + 1)
    return total
