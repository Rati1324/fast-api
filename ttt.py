x = "X-00X---X"

def method_1():
    player_moves = {
        "X" : [0,0,0,0,0,0,0,0],
        "0" : [0,0,0,0,0,0,0,0]
    }

    for i in range(len(x)):
        if x[i] != "-":
            cur_player = player_moves[x[i]]
            if i//3 == 0:
                col = i+3
                cur_player[0] += 1
                cur_player[i+3] += 1

                if col == 3:
                    cur_player[6] += 1
                elif col == 5:
                    cur_player[7] += 1

            elif i//3 == 1:
                col = i
                cur_player[1] += 1
                cur_player[i] += 1

                if col == 4:
                    cur_player[6] += 1
                    cur_player[7] += 1

            elif i//3 == 2:
                col = 3+i%3
                cur_player[2] += 1
                cur_player[3+i%3] += 1

                if col == 3:
                    cur_player[7] += 1
                elif col == 5:
                    cur_player[6] += 1

    for key, value in player_moves.items():
        for i in value:
            if i == 3:
                print(f"{key} is the winner")
                return

def method_2():
    positions = [[0, 1, 2],
                [3, 4, 5],
                [6, 7, 8],
                [0, 3, 6],
                [1, 4, 7],
                [2, 5, 8],
                [0, 4, 8],
                [2, 4, 6],]
    for i in positions:
        a, b, c = i
        if x[a] != '-' and x[a] == x[b] and x[b] == x[b]:
            print(f"{x[a]} is the winner")
            return

method_2()