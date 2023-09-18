def splitChar(strVal):
    result = []
    for char in strVal:
        result.append(char)
    return result


def remCharMatch(Name_1, Name_2):
    Name_1, Name_2 = splitChar(Name_1.upper()), splitChar(Name_2.upper())
    common = set()
    for char in Name_1:
        for char_2 in Name_2:
            if char == char_2:
                common.add(char)
    common = list(common)
    for i in range(len(common)):
        Name_1.remove(common[i])
        Name_2.remove(common[i])
    result = (len(Name_1) + len(Name_2)) - 1
    return result


def findRelation(num):
    FLAMES_1 = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
    FLAMES_2 = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
    FLAMES_3 = []
    for i in range(5):
        if i % 2 == 0:
            for item in FLAMES_2:
                for relation in FLAMES_1:
                    if item == relation:
                        FLAMES_3.append(item)
            FLAMES_1 = FLAMES_3.copy()
            FLAMES_3.clear()
        else:
            FLAMES_1.insert(0, FLAMES_1[-1])
            FLAMES_1.pop(-1)
        if len(FLAMES_1) > num:
            FLAMES_1.pop(num)
        else:
            num = len(FLAMES_1) - num
            FLAMES_1.pop(num)
    return FLAMES_1[0]


if __name__ == "__main__":
    name_1 = input("Name of Person_1: ")
    name_2 = input("Name of Person_2: ")
    num = remCharMatch(name_1, name_2)
    print("Relation:", findRelation(num))
