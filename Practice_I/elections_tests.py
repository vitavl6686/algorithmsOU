global tests

tests = [
    [['Alice', 'Bob', 'Bob', 'Alice'], "second_round", "2 of 2 tied error "],
    [['Alice', 'Bob', 'Alice', 'Alice'], "Alice", '1 of 2 wins'],
    [['Bob', 'Chan', 'Chan', 'Alice'], "Chan", '1 of 3 wins'],
    [[], "second_round", "empty votes"],
    [["Alice", "Alice"], "Alice", "one candidate"]
]