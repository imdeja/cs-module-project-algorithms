'''
Input: a List of integers where every int except one shows up twice
Returns: an integer
'''
def single_number(arr):
    return 2 * sum(set(arr)) - sum(arr)
    # Ran 1 test in 0.001s




if __name__ == '__main__':
    # Use the main function to test your implementation
    arr = [1, 1, 4, 4, 5, 5, 3, 3, 9, 0, 0]

    print(f"The odd-number-out is {single_number(arr)}")