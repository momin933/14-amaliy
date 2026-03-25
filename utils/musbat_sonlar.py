def filtr(sonlar):
    yangi_ruyxat = []
    for son in sonlar:
        if son > 0:
            yangi_ruyxat.append(son)
    return yangi_ruyxat

if __name__ == "__main__":
    test_list = [-5, 10, 0, 3, -1, 8]
    print(f"Asl: {test_list} -> Filtrlangan: {filtr(test_list)}")