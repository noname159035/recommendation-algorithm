import tkinter.messagebox as mb


bin = ['.', '\'', '\"', '[', ']', '(', ')', '{', '}', '<', '>', ':', ',', '-', '!', '?', ';', '/', '\\',
       '@', '#', '$', '%', '^', '&', '*', '+', '=', '_', '|', '~', '`', '\n']


def show_info():
    mb.showinfo("обновление списка", "после обновления списка необходимо перезагрузить преложение")


def save_data(data_loc):
    file = open("data.txt", "w")
    for elem in data_loc:
        file.write(elem + " " + str(data_loc[elem]) + "\n")
    file.close()


def load_text_data(lines):
    text_data = []
    i = 0
    while i < len(lines):
        lines[i] = lines[i].replace('\n', '')
        for elem in bin:
            lines[i] = lines[i].replace(elem, '')
        if lines[i] == '':
            lines.pop(i)
            i -= 1
        i += 1
        if i % 2 != 0:
            text_data.append([lines[i - 1], lines[i]])
    return text_data


def load_data_best():
    loc_data = []


def load_data():
    data_loc = {}
    file = open("data.txt", "r").readlines()
    for elem in file:
        elem = elem.replace("\n", "")
        elem = elem.split()
        data_loc[elem[0]] = int(elem[1])
    # print(data_loc)
    return data_loc


def learn_up(line):
    data_loc = load_data()
    check = line.split(" ")
    if line[len(line) - 1] == " ":
        line = line[:-1]
    for elem in bin:
        line = line.replace(elem, '')
    if len(check) == 1:
        if line in data_loc:
            data_loc[line] += 1
        else:
            data_loc[line] = 1
            save_data(data_loc)
            data_loc = load_data()
        if data_loc[line] > 100:
            data_loc[line] = 100
        print("[LOG] СЛОВАРЬ ПОПОЛНЕН СЛОВОМ (" + line + ")")
        # print(data_loc)

    elif len(check) > 1:
        line = line.split(" ")
        new = 0
        for word in line:
            if word in data_loc:
                data_loc[word] += 1
            else:
                data_loc[word] = 1
                save_data(data_loc)
                data_loc = load_data()
                new += 1
            if data_loc[word] > 100:
                data_loc[word] = 100
        print("[LOG] СЛОВАРЬ ПОПОЛНЕН СПИСКОМ СЛОВ #" + str(new))
        # print(data_loc)
    return data_loc


def learn_down(line):
    data_loc = load_data()
    if line[len(line) - 1] == " ":
        line = line[:-1]
    for elem in bin:
        line = line.replace(elem, '')
    check = line.split(" ")
    if len(check) == 1:
        if line in data_loc:
            data_loc[line] -= 1
        else:
            data_loc[line] = -1
            save_data(data_loc)
            data_loc = load_data()
        if data_loc[line] < -50:
            data_loc[line] = -50
        print("[LOG] СЛОВАРЬ ПОПОЛНЕН СЛОВОМ (" + line + ")")
        # print(data_loc)

    elif len(check) > 1:
        line = line.split(" ")
        new = 0
        for word in line:
            if word in data_loc:
                data_loc[word] -= 1
            else:
                data_loc[word] = 0
                save_data(data_loc)
                data_loc = load_data()
                new += 1
            if data_loc[word] < -30:
                data_loc[word] = -30
        print("[LOG] СЛОВАРЬ ПОПОЛНЕН СПИСКОМ СЛОВ #" + str(new))
        # print(data_loc)
    return data_loc


def rec(line):
    data = load_data()
    KH = 0
    k = 0
    for elem in line:
        try:
            KH += data[elem]
            k += 1
        except KeyError:
            data = learn_up(elem)
            print("[LOG] СЛОВАРЬ ПОПОЛНЕН")
            # print(data)
    return KH / k


def load_rec():
    file = open("C:\\Users\\User\\Desktop\\shar_best.txt", 'w', encoding='utf-8')
    lines = open("C:\\Users\\User\\Desktop\\shar.txt", encoding='utf-8').readlines()

    text_data = load_text_data(lines)
    # print(text_data)

    for i in range(len(text_data)):
        try:
            buf = text_data[i][0].replace('Вопрос ', '')
            if rec(buf.split()) > 40:
                file.write(text_data[i][0] + '\n' + text_data[i][1] + '\n')
                print("[LOG] Список реков обновлен")
        except ZeroDivisionError:
            pass
    file.close()
    show_info()

def get_best():
    lines = open("C:\\Users\\User\\Desktop\\shar_best.txt", encoding='utf-8').readlines()
    data_best = load_text_data(lines)
    return data_best


def save_id(id):
    file = open("save.txt", 'w')
    file.write(id)
    file.close()


def load_id(id):
    file = open("save.txt").readline()
    id = int(file.replace('\n', ''))
    return id