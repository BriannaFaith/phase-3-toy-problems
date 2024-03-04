def solution(N):
    alphabet = "abcdefghijklmnopqrstuvwxyz" # alphabet as a string
    # Get the length of the alphabet
    alphabet_length = len(alphabet)
    result = "" # empty string for result.

    # Repeat the pattern of letters until the desired length is reached
    for i in range(N):
        # Repeats the pattern when N is greater than the length of the alphabet
        result += alphabet[i % alphabet_length]

    return result

print(solution(77))

