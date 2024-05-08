import numpy as np

# i wanted to generate pairs for teams to play against each other in 5 rounds, across 5 activities


def random_latin_square(n):
    # Start with an empty n x n array
    square = np.zeros((n, n), dtype=int)

    # Initialize the first row with a random permutation of numbers from 1 to n
    square[0] = np.random.permutation(n) + 1

    # Attempt to fill in the rest of the square
    for i in range(1, n):
        for attempt in range(100):  # Limit attempts to avoid infinite loops
            # Shuffle the first row to get a new row
            row = np.random.permutation(n) + 1
            if all(row[j] not in square[:i, j] for j in range(n)):  # Check column constraints
                square[i] = row
                break
        else:
            # If no valid row is found after 100 attempts, start over
            return random_latin_square(n)

    return square


def generate_pair_grid(L1, L2):
    """ Generate a grid with unique pairs from two Latin squares """
    n = L1.shape[0]
    # Create an empty grid of tuples
    pair_grid = np.empty((n, n), dtype=object)
    pairs = set()
    count = 0
    for i in range(n):
        for j in range(n):
            pair = (L1[i, j], L2[i, j])
            if pair not in pairs:
                pair_grid[i, j] = pair
                pairs.add(pair)
            else:
                count += 1
                if count > 0:
                    raise KeyError("failed")
    return pair_grid


def main():
    # Generate two Latin squares
    for attempt in range(10000):
        L1 = random_latin_square(5)
        L2 = random_latin_square(5) + 5  # Offset by 5 to get numbers 6-10

        # Print results
        print("Latin Square 1:")
        print(L1)
        print("Latin Square 2:")
        print(L2)

        # Generate a grid of unique pairs
        print("Pair Grid:")
        try:
            pair_grid = generate_pair_grid(L1, L2)
        except KeyError:
            print("fail")
            continue
        print("success!")
        for row in pair_grid:
            print(" ".join(str(x) for x in row))
        break


if __name__ == "__main__":
    main()
