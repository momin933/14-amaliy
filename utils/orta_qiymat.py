def orta(sonlar):
    if not sonlar:
        return 0
    return sum(sonlar) / len(sonlar)

if __name__ == "__main__":
    print(f"O'rtacha: {orta([10, 20, 30])}") # 20.0
    print(f"Bo'sh ro'yxat: {orta([])}")      # 0