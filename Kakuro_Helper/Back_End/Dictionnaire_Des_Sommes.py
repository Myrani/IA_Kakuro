import pickle

# Ancienne version de la fonction présente dans Divided_Label


def findCommonNumberForLength(dictionnaire_Des_Sommes, firstNumber, firstLen, secondNumber, secondLen):

    set_One = []
    set_Two = []

    for combinaison_First in dictionnaire_Des_Sommes[firstNumber]:
        if len(combinaison_First) == firstLen:
            for el in combinaison_First:
                set_One.append(el)

    for combinaison_Second in dictionnaire_Des_Sommes[secondNumber]:
        if len(combinaison_Second) == secondLen:
            for el in combinaison_Second:
                set_Two.append(el)

    set_One = set(set_One)
    set_Two = set(set_Two)

    return set_One & set_Two


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
