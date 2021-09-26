from defs import *
import tkinter as tk



def good():
    line = text.get('1.0', tk.END)
    line = line.split('Шар говорит:')[0]
    line = line.replace('\n', '')
    line = line.replace('Вопрос: ', '')
    line = line.replace('Вопрос ', '')
    # print(line)
    data = learn_up(line)
    save_data(data)
    get_new()
    # print('good')


def get_KH():
    line = text.get().split()
    rec(line)
    # print('kh')


def not_good():
    line = text.get('1.0', tk.END)
    line = line.split('Шар говорит:')[0]
    line = line.replace('\n', '')
    line = line.replace('Вопрос: ', '')
    line = line.replace('Вопрос ', '')
    data = learn_down(line)
    save_data(data)
    get_new()
    # print('not good')


def get_new():
    try:
        id = int(open('save.txt').readline())
        text.delete("1.0", tk.END)
        text.insert('1.0', text_data[id][0] + '\n')
        text.insert('2.0', text_data[id][1])
        id += 1
        file = open('save.txt', 'w')
        file.write(str(id))
        file.close()
    except IndexError:
        text.delete("1.0", tk.END)
        text.insert('1.0', "Данные закончились :c")


def get_new_best():
    try:
        id = int(open('saveBest.txt').readline())
        text.delete("1.0", tk.END)
        text.insert('1.0', data_best[id][0] + '\n')
        text.insert('2.0', data_best[id][1])
        id += 1
        file = open('saveBest.txt', 'w')
        file.write(str(id))
        file.close()
    except IndexError:
        text.delete("1.0", tk.END)
        text.insert('1.0', "Данные закончились :c")


lines = open("C:\\Users\\User\\Desktop\\shar.txt", encoding='utf-8').readlines()
text_data = load_text_data(lines)

f = open('saveBest.txt', 'w')
f.write('0')
f.close()

data_best = get_best()

window = tk.Tk()

window.title("SHAR")
window.geometry('400x250')
window.resizable(width=False, height=False)
window['bg'] = "#3191BB"

text = tk.Text(window, width=38, height=7)
text.place(x=45, y=30)

get_new()

btn1 = tk.Button(window, text="✔", command=good, font=180)
btn1.place(x=110, y=153)

btn2 = tk.Button(window, text="SKIP", command=get_new, font=180)
btn2.place(x=175, y=153)

btn3 = tk.Button(window, text="Х", command=not_good, font=180)
btn3.place(x=260, y=153)

btn4 = tk.Button(window, text="Обновить реки", command=load_rec, font=180)
btn4.place(x=30, y=200)

btn5 = tk.Button(window, text="Рекомендовать", command=get_new_best, font=180)
btn5.place(x=220, y=200)


window.mainloop()
