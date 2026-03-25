def hisobla(a, b, amal):
    if amal == "+":
        return a + b
    elif amal == "-":
        return a - b
    elif amal == "*":
        return a * b
    elif amal == "/":
        if b != 0:
            return a / b
        else:
            return "Xato: Nolga bo'lish mumkin emas!"
    else:
        return "Noma'lum amal"

if __name__ == "__main__":
    print(f"10 + 5 = {hisobla(10, 5, '+')}")
    print(f"20 / 4 = {hisobla(20, 4, '/')}")