from tkinter import *
from tkinter import messagebox
import sqlite3

def Insert():
    con = sqlite3.connect("md202310620")
    cur = con.cursor()
    cur.execute("create table if not exists userTable(id char(4), userName char (15), email char(15), birthYear int)")

    data1 = entry1.get()
    data2 = entry2.get()
    data3 = entry3.get()
    data4 = entry4.get()

    if data1 == '' or data2 == '' or data3 == '' or data4 == '':
        messagebox.showerror("오류", "모든 입력란에 데이터를 입력하세요")
    elif data1 in List:
        messagebox.showerror("오류", "데이터 입력에 오류가 발생함(중복된 아이디 존재)")
    else:
        List.append(data1)
        sql = "insert into userTable values('" + data1 + "','" + data2 + "','" + data3 + "'," + data4 + ")"
        cur.execute(sql)
        messagebox.showinfo("성공", "데이터 입력 성공")
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
    con.commit()
    con.close()

def Check():
    con = sqlite3.connect("md202310620")
    cur = con.cursor()

    cur.execute("select * from userTable")
    row = cur.fetchall()

    if not row:
        messagebox.showerror("오류", "조회할 데이터가 없습니다")
    else:
        # 리스트박스 안의 데이터 삭제
        listbox1.delete(0, END)
        listbox2.delete(0, END)
        listbox3.delete(0, END)
        listbox4.delete(0, END)

        # 재삽입
        listbox1.insert(END, "사용자ID\n", "-----------")
        listbox2.insert(END, "사용자이름\n", "-----------")
        listbox3.insert(END, "이메일\n", "-----------")
        listbox4.insert(END, "출생연도\n", "-----------")

        for i in row:
            index1, index2, index3, index4 = i

            listbox1.insert(END, index1)
            listbox2.insert(END, index2)
            listbox3.insert(END, index3)
            listbox4.insert(END, index4)

    con.close()

window = Tk()
window.title("GUI 데이터 입력")
window.geometry("660x333")

List = []

entry1 = Entry(window, width=10)
entry2 = Entry(window, width=10)
entry3 = Entry(window, width=10)
entry4 = Entry(window, width=10)

button1 = Button(window, text='입력', command=Insert)
button2 = Button(window, text='조회', command=Check)

listbox1 = Listbox(window, width=23, height=18, bg='yellow')
listbox2 = Listbox(window, width=23, height=18, bg='yellow')
listbox3 = Listbox(window, width=23, height=18, bg='yellow')
listbox4 = Listbox(window, width=23, height=18, bg='yellow')

entry1.pack()
entry2.pack()
entry3.pack()
entry4.pack()
button1.pack()
button2.pack()
listbox1.pack()
listbox2.pack()
listbox3.pack()
listbox4.pack()

entry1.place(x=80, y=10)
entry2.place(x=180, y=10)
entry3.place(x=280, y=10)
entry4.place(x=380, y=10)

button1.place(x=480, y=5)
button2.place(x=540, y=5)

listbox1.place(x=0, y=40)
listbox2.place(x=165, y=40)
listbox3.place(x=330, y=40)
listbox4.place(x=495, y=40)

window.mainloop()