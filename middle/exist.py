def exist(board, word):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(i, j, k):
        if board[i][j] != word[k]:
            return False
        if k == len(word) - 1:
            return True

        visited.add((i, j))
        flag = False
        for d_i, d_j in directions:
            new_i, new_j = i + d_i, j + d_j
            if 0 <= new_i < m and 0 <= new_j < n:
                if (new_i, new_j) not in visited:
                    if dfs(new_i, new_j, k + 1):
                        flag = True
                        break

        visited.remove((i, j))
        return flag

    m = len(board)
    n = len(board[0])
    visited = set()
    for i in range(m):
        for j in range(n):
            if dfs(i, j, 0):
                return True
    return False


print(exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))
print(exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"))
print(exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"))
