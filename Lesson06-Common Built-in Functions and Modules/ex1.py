def eight_queens(list):
    for i in range(0, 7):
        for j in range(0, 7):
            if(i != j):
                if(list[i][0] == list[j][0] or list[i][1] == list[j][1]):
                    return False
                if(abs(list[i][0] - list[j][0]) == abs(list[i][1] - list[j][1])):
                    return False
    return True

print(eight_queens([[0, 0], [1, 4], [2, 7], [3, 5], [4, 2], [5, 6], [6, 1], [7, 3]]))