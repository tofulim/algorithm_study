def get_turn_cnt(board):
    string_board = ''.join(board)

    o_cnt = string_board.count("O")
    x_cnt = string_board.count("X")

    return o_cnt, x_cnt


def _get_game_status(board):
    player2win_cnt = {
        "O": 0,
        "X": 0,
        ".": 0,
    }

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            player2win_cnt[board[i][0]] += 1

        if board[0][i] == board[1][i] == board[2][i]:
            player2win_cnt[board[0][i]] += 1

    if board[0][0] == board[1][1] == board[2][2]:
        player2win_cnt[board[1][1]] += 1
    if board[0][2] == board[1][1] == board[2][0]:
        player2win_cnt[board[1][1]] += 1

    return player2win_cnt


def is_possible(o_cnt, x_cnt, board):
    player2win_cnt = _get_game_status(board)

    o_win_cnt = player2win_cnt["O"]
    x_win_cnt = player2win_cnt["X"]

    # cnt error
    if x_cnt > o_cnt or abs(o_cnt - x_cnt) >= 2:
        return 0
    # 개수에 문제가 없고 게임이 끝나지 않았으면 정상
    if o_win_cnt == 0 and x_win_cnt == 0:
        return 1
    # o가 이긴 정상적인 경우
    if o_win_cnt > 0 and x_win_cnt == 0 and o_cnt == x_cnt + 1:
        return 1
    # x가 이긴 정상적인 경우
    if x_win_cnt > 0 and o_win_cnt == 0 and x_cnt == o_cnt:
        return 1

    return 0


def solution(board):
    answer = -1
    o_cnt, x_cnt = get_turn_cnt(board)

    return is_possible(o_cnt, x_cnt, board)