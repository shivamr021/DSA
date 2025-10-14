def ticTacToeWinner(moves, n):
    row = [0] * 3
    col = [0] * 3
    diag = anti_diag = 0

    for i, (r, c) in enumerate(moves):
        val = 1 if i % 2 == 0 else -1 

        row[r] += val
        col[c] += val
        if r == c:
            diag += val
        if r + c == 2:
            anti_diag += val

        if 3 in (row[r], col[c], diag, anti_diag):
            return "player1"
        if -3 in (row[r], col[c], diag, anti_diag):
            return "player2"

    if len(moves) < 9:
        return "uncertain"
    return "draw"
