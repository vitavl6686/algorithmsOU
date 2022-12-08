import pangram_tests
import pangram
import elections_tests
import elections
import voucher_tests
import voucher

#pangram.py testing
is_passed = True
for case in pangram_tests.tests:
    result = pangram.missed_letters(case[0])
    if result != case[1]:
        print(case[2] + " error")
        print("input: " + case[0])
        print("expected: "+ case[1])
        print("got: " + result)
        is_passed = False
if(is_passed):
    print("pangram tests passed")


#elections.py testing
is_passed = True
for case in elections_tests.tests:
    result = elections.find_winner(case[0])
    if result != case[1]:
        print(case[2] + " error")
        print("input: " + "".join(case[0]))
        print("expected: "+ case[1])
        print("got: " + result)
        is_passed = False
if(is_passed):
    print("elections tests passed")


#voucher.py testsing
is_passed = True
for case in voucher_tests.tests:
    result = voucher.find_pairs(case[0], case[1])
    if result != case[2]:
        print(case[3] + " error")
        print("input: " + str(case[0])+ ", "+ str(case[1]))
        print("expected: "+ str(case[2]))
        print("got: " + str(result))
        is_passed = False
if(is_passed):
    print("voucher tests passed")
