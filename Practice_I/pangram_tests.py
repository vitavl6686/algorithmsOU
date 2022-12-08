
global tests
tests = [
    ["bcd fgh jklmn pqrst vwxyz", "aeiou", "no vowels"],
    ["", "abcdefghijklmnopqrstuvwxyz", "empty string"], 
    ["abcdefghijklmnopqrstuvwxyz", "", "all letters"],
    ["abcdeeefghijklmnpqrstuvwxyz", "o", "with doubled letters"]
]