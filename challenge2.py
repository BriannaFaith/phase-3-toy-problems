def solution(A):
    sums_of_digits = {} # creating a dictionary to store sum of digits for every number
    max_sum = -1 # set the max_sum to -1

    for num in A: # #Calculate sum of digits in each number
        sum_of_digits = sum(int(digit) for digit in str(num))

        if sum_of_digits in sums_of_digits: #Check if the sum of digits is present in sums_of_digits
            max_sum = max(max_sum, num + sums_of_digits[sum_of_digits]) # set the max_sum to maximum of current max_sum and sum of current number and number from dictionary

        #Set the dictionary with the maximum number for the current sum of digits
        sums_of_digits[sum_of_digits] = max(sums_of_digits.get(sum_of_digits, num), num)

    return max_sum 


# Example usage:
A = [51, 71, 17, 42]


print(solution(A))
