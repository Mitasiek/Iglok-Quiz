from tkinter import *


window = Tk()
window.geometry("800x600")
window.title("Iglok Quiz Game")




icon = PhotoImage(file='Banan.png')
window.iconphoto = (False, icon)
window.config(background="#BAC6CF")


label = Label(window, text="Iglok Quiz Game", font=('Arial',  40, 'bold'),fg='#625FEA', bg="#BAC6CF",)
label.pack()
label1 = Label(window, text="1. Kto zazwyczaj jest ostatni w tabeli? ", font=('Arial', 20), pady=25, bg="#BAC6CF")
label1.pack()

def Window2():
        window2 = Tk()
        window.destroy()
        window2.geometry("800x600")
        window2.title("Iglok Quiz Game")
        window2.config(background="#BAC6CF")

        labelw2 = Label(window2, text="Iglok Quiz Game", font=('Arial',  40, 'bold'),fg='#625FEA', bg="#BAC6CF")
        labelw2.pack()
        labelw21 = Label(window2, text="2. Jaka postać jest najniższa?? ", font=('Arial', 20), pady=25, bg="#BAC6CF")
        labelw21.pack()
        window2.mainloop()

def WrongAnswer():
    label2 = Label(window, text="Zła Odpowiedź",font=('Arial', 20, 'bold') , bg="#BAC6CF", fg="red")
    label2.place(x=300, y=325)


button = Button(window,
                text='a) Adolf',
                font=('Arial', 13, 'bold'),
                command=WrongAnswer,
                bg='#96ABD9',
                activebackground='#899DC7',
                relief='ridge',
                padx=16).pack()
button2 = Button(window,
                text='b) Dupson',
                font=('Arial', 13, 'bold'),
                command=Window2,
                activebackground='#899DC7',
                bg='#96ABD9',
                justify=LEFT,
                relief='ridge',
                padx=6).pack()
button3 = Button(window,
                text='c) Cinuszek',
                font=('Arial', 13, 'bold'),
                command=WrongAnswer,
                bg='#96ABD9',
                activebackground='#899DC7',
                justify=LEFT,
                relief='ridge').pack()


window.mainloop()