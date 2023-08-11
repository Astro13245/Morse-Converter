en = ""
m = ""


def translateEn():
    global m, en

    en = input("Enter what you want translated: ")

    for l in en:

        l = l.upper()
        if l == "A":
            m += "•-"
        if l == "B":
            m += "-•••"
        if l == "C":
            m += "-•-•"
        if l == "D":
            m += "-••"
        if l == "E":
            m += "•"
        if l == "F":
            m += "••-•"
        if l == "G":
            m += "--•"
        if l == "H":
            m += "••••"
        if l == "I":
            m += "••"
        if l == "J":
            m += "•---"
        if l == "K":
            m += "-•-"
        if l == "L":
            m += "•-••"
        if l == "M":
            m += "--"
        if l == "N":
            m += "-•"
        if l == "O":
            m += "---"
        if l == "P":
            m += "•--•"
        if l == "Q":
            m += "--•-"
        if l == "R":
            m += "-•-"
        if l == "S":
            m += "•••"
        if l == "T":
            m += "-"
        if l == "U":
            m += "••-"
        if l == "V":
            m += "•••-"
        if l == "W":
            m += "•--"
        if l == "X":
            m += "-••-"
        if l == "Y":
            m += "-•--"
        if l == "Z":
            m += "--••"
        if l == "0":
            m += "-----"
        if l == "1":
            m += "•----"
        if l == "2":
            m += "••---"
        if l == "3":
            m += "•••--"
        if l == "4":
            m += "••••-"
        if l == "5":
            m += "•••••"
        if l == "6":
            m += "-••••"
        if l == "7":
            m += "--•••"
        if l == "8":
            m += "---••"
        if l == "9":
            m += "----•"
        if l == "?":
            m += "••--••"
        if l == "!":
            m += "-•-•--"
        if l == ".":
            m += "•-•-•-"
        if l == ",":
            m += "--••--"
        if l == ";":
            m += "-•-•-•"
        if l == ":":
            m += "---•••"
        if l == "+":
            m += "•––"
        if l == "-":
            m += "-••••-"
        if l == "/":
            m += "-••-•"
        if l == "=":
            m += "-•••-"
        if l == " ":
            m += " "
        m += " "

    print(m)
    m = ""


def translateM():
    global m, en
    translating = ""
    i = 0

    m = input("Enter what you want to translate: ")

    for c in m:

        if c == " " and i == 0:
            en += " "
        elif c == " " and i != 0:
            # en += translatingM(translating)
            print(translating)
            translating = ""
        else:
            translating += c
        i += 1
    print(translating)


# def translatingM(translating):

#     if translating == "•-":
#         en += "a"
#     elif translating == "":
#         en += ""


translateM()
