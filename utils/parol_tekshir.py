def kuchlimi(parol):
    if len(parol) >= 8:
        return "Kuchli"
    else:
        return "Kuchsiz"

if __name__ == "__main__":
    print(f"12345: {kuchlimi('12345')}")       # Kuchsiz
    print(f"admin123: {kuchlimi('admin123')}") # Kuchli