def uzunlik(matn):
    if not matn:
        return "Bo'sh matn"
    return len(matn)

if __name__ == "__main__":
    print(f"Uzunlik: {uzunlik('Salom')}") # 5
    print(f"Uzunlik: {uzunlik('')}")      # Bo'sh matn