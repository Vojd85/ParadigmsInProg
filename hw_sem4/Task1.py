def corellation(lst_1: list, lst_2: list):
    medium_1 = sum(lst_1) / len(lst_1)
    medium_2 = sum(lst_2) / len(lst_2)
    
    def diff_nomerator(x: int, y: int):
        return (x - medium_1) * (y - medium_2)
    
    nomerator = sum(list(map(diff_nomerator, lst_1, lst_2)))
    denomerator = (sum(list(map(lambda x: (x - medium_1)**2, lst_1))) * \
                    sum(list(map(lambda x: (x - medium_2)**2, lst_2)))) ** 0.5
    
    return nomerator / denomerator

if __name__ == "__main__":
    lst_1 = [2, 4, 6, 8]
    lst_2 = [2, 4, 10, 12]

    print(corellation(lst_1, lst_2))