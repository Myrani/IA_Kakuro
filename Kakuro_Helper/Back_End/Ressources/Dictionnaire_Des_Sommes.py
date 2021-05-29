import pickle


def generateDictionnaire():
    dictionnaire_Des_Sommes = {}

    for i in range(0, 46):
        dictionnaire_Des_Sommes[i] = []
    # Personnes ne devrai avoir à faire ça
    for a in range(1, 10):
        for b in range(1, 10):
            for c in range(1, 10):
                for d in range(1, 10):
                    for e in range(1, 10):
                        for f in range(1, 10):
                            for g in range(1, 10):
                                for h in range(1, 10):
                                    for i in range(1, 10):
                                        current_set = set(
                                            [a, b, c, d, e, f, g, h, i])
                                        if current_set not in dictionnaire_Des_Sommes[sum(current_set)]:
                                            dictionnaire_Des_Sommes[sum(
                                                current_set)].append(current_set)

    for el in dictionnaire_Des_Sommes:
        print(el, dictionnaire_Des_Sommes[el])

    with open('dictionnaire.pkl', 'wb') as dictionnaire:
        pickle.dump(dictionnaire_Des_Sommes, dictionnaire)

    return None
