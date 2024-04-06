from collections import Counter
import statistics

def calculate_mean(arr):
    return sum(arr) / len(arr)

def calculate_median(arr):
    return statistics.median(arr)

def calculate_mode(arr):
    count = Counter(arr)
    mode = count.most_common(1)[0][0]
    return mode

def main():
    test_cases = [
        [16, 18, 27, 16, 23, 21, 19],
        [26, 28, 37, 26, 33, 31, 29],
        [1.6, 1.8, 2.7, 1.6, 2.3, 2.1, 0.19],
        [0, 160, 180, 270, 160, 230, 210, 190, 0],
        [20, 18, 18, 27, 16, 27, 27, 19, 20],
        [1000, 100, 1000, 100, 1000, 100, 1000, 100, 1000]
    ]

    for i, arr in enumerate(test_cases, start=1):
        print(f"Test case {i}:")
        print("Array of elements =", arr)
        print("Mean =", calculate_mean(arr))
        print("Median =", calculate_median(arr))
        print("Mode =", calculate_mode(arr))
        print()

if __name__ == "__main__":
    main()
