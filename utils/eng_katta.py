def top(sonlar):
    if not sonlar:
        return "Ro'yxat bo'sh"
    return max(sonlar)

if __name__ == "__main__":
    print(f"Eng kattasi: {top([5, 12, 8, 21, 3])}") # 21