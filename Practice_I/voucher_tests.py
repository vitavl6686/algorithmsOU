
F1 = ('food', 1)
F2 = ('food', 2)
F5 = ('food', 5)
F6 = ('food', 6)
T5 = ('toy', 5)

tests = [
    [[], 5, set(), "an empty shop"],
    [[F5], 5, set(), "no pairs"],
    [[F1,F5,F2,F6], 9, set(), "no match"],
    [[F1,F5,F2,F6], 3, set([(F1,F2),]), "1 pair"],
    [[F1,F5,F2,F6], 7, set([(F1,F6), (F2, F5)]), "2 pairs"],
    [[F1,F5,F2,T5], 10, set([(F5,F5), (F5,T5), (T5,T5)]), "same price"]
]
