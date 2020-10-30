# import os

def printboard(board, currentblock, dead):
    # os.system("clear")
    for i in board:
        if i[0:2] == "Cc" or i[0:2] == "Fc" or i[0:2] == "Ic":
            print(board[i] + "  ", end=i[2])
            if i != "Ic1":
                if i[2] == "1":
                    print("\n\u001B[107m                                     \u001B[0m")
                else:
                    print(end="\n")
                    for k in range(-2, 1):
                        x = chr(ord(i[0]) + k)
                        if x not in dead:
                            if x != currentblock:
                                print(end="---|---|---")
                            else:
                                print(end="\u001B[92m---|---|---\u001B[0m")
                        else:
                            print(board[x + "b2"][0:5], end="           \u001B[0m")
                        if x != i[0]:
                            print(end="\u001B[107m  \u001B[0m")
                        else:
                            print()
            else:
                print("\n", "a   b   c    a   b   c    a   b   c")
        else:
            if i[1] == "c":
                print(board[i], end="\u001B[107m  \u001B[0m")
            else:
                if i[0] == currentblock:
                    print("\u001B[92m" + board[i], end="\u001B[92m|\u001B[0m")
                else:
                    if i[0] in dead:
                        print(board[i] + board[i][0:5], end=" \u001B[0m")
                    else:
                        print(board[i], end="|")
    print("\n")  # formatting

# notes: 31 pink, 32 green, 33 orange, 34 darkest blue, 35 purple, 36 lighter but not light blue, 91 red, 92 slightly
# less neon green, 93 orangey yellow, 94 blue, 95 lavender, 96 electric blue
