# Made by Aayog Koirala
from tkinter import*
import time

name = {}

xPlayer = "   X   "
Oplayer = "   O   "


def button(row, col, i):
    name[i] = Button(frame, text="         ", command=lambda: checker(name[i]))
    name[i].grid(row=row, column=col, sticky=N+E+W+S)


def printWin(toPrint):
    label_1 = Label(frame, text=toPrint)
    label_1.grid(row=10, column=0, sticky=N+E+W+S)

    button_1 = Button(frame, text="Again", command=lambda: new_game())
    button_1.grid(row=11, column=0, sticky=N+E+W+S)

    button_2 = Button(frame, text="Quit", command=lambda: quit_1())
    button_2.grid(row=11, column=1, sticky=N+E+W+S)


def quit_1():
    root.destroy()


def new_game():
    root.destroy()
    main()


def val(i):
    return name[i]['text']


def wins(total_arr):
    chunks = [total_arr[x:x+3] for x in range(0, len(total_arr), 3)]
    for items in chunks:
        x, y, z = items
        if val(x) != "         " and len(set([val(x), val(y), val(z)])) == 1:
            printWin(f"{'X' if val(x) == xPlayer else 'O'} wins")
    return False


def tie():
    if "         " not in [name[x]['text'] for x in range(1, 10)]:
        return True


def checker(button):
    global user
    buttonX = button
    if user == xPlayer and buttonX['text'] == "         ":
        buttonX['text'] = xPlayer
        user = user_reverse(user)
    elif buttonX['text'] == "         " and user == Oplayer:
        buttonX['text'] = Oplayer
        user = user_reverse(user)
    label_name = Label(root, text=user + "'s turn")
    label_name.grid(row=0, column=0)
    wins([1, 2, 3, 1, 4, 7, 1, 5, 9, 2, 5, 8, 3, 6, 9, 4, 5, 6, 7, 8, 9])
    if(tie()):
        printWin("Tie!!")


def sleep(t=2):
    time.sleep(t)


def user_reverse(usr):
    return xPlayer if usr == Oplayer else Oplayer


def main():
    global root, frame, button_1, user
    root = Tk()
    root.wm_title('TicTacToe')
    root.geometry('240x180')
    user = xPlayer
    label_name = Label(root, text=user + "'s turn")
    label_name.grid(row=0, column=0)
    frame = Frame(root)
    frame.grid(row=1, column=0)
    button_1 = ['button{}'.format(x) for x in range(1, 10)]
    buttons = StringVar()
    r = c = 0
    count = 1
    for i in button_1:
        button(r, c, count)
        c += 1
        if c == 3:
            r += 1
            c = 0
        count += 1
    root.mainloop()


if __name__ == "__main__":
    main()
