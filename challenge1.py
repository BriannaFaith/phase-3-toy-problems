def solution(A):
    total_bricks = sum(A)
    N = len(A) # number of boxes
    target_bricks = 10 # target of bricks required in each box
    moves = 0 # initialize number of moves, set it to 0.

    # check if total number of bricks is divisible by number of boxes
    if total_bricks % N != 0:
        return -1

    for i in range(N): # Iterate through each box
        diff = A[i] - target_bricks # difference between number of bricks and target bricks
        if diff > 0: # checking for excess bricks
            if i > 0: # Check if the current box is not the first box
                move_left = min(diff, A[i - 1] - target_bricks) # set to the minimum of the difference between the current box and the target bricks, and the difference between the left box and the target number of bricks
                A[i - 1] -= move_left # move the excess brick to the left box
                moves += move_left # update number of moves
                A[i] -= move_left
            else: # Current box is the first box, cannot move left
                return -1
        elif diff < 0: # deficient of the targeted bricks
            if i < N - 1: # Check if the current box is not the last box
                move_right = min(abs(diff), A[i + 1] - target_bricks) # set to the minimum of the absolute difference between the current box and the target bricks, and the difference between the right box and the target number of bricks
                
                A[i + 1] -= move_right # move bricks to the right
                moves += move_right # update number of moves
                A[i] += move_right
            else: # Current box is the last box, cannot move right
                return -1
            print("Bricks in boxes:", A)

    return moves

A = [11, 10, 8, 12, 8, 10, 11]
print(solution(A))
