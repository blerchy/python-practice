import problem2 as p

def test(num, A, expected, actual):
    if expected == actual:
        print("Test #" + str(num) + " passed.")
    else:
        print("TEST #" + str(num) + " FAILED!")
        print("For A = " + str(A) + ", expected " + str(expected) + " but got " + str(actual) + ".")
        exit(0)

def main():
    print("Begin regular test cases")
    print("------------------------")
    # Test 1
    A = [1,2,3,4,5]
    test(1, A, [120, 60, 40, 30, 24], p.problem2(A))

    # Test 2
    A = [3,2,1]
    test(2, A, [2, 3, 6], p.problem2(A))

    # Test 3
    A = [1,-1,1,-1,1,1,-1,-1]
    test(3, A, A, p.problem2(A))

    # Test 4
    A = [-3,4,-8]
    test(4, A, [-32,24,-12], p.problem2(A))

    # Test 5
    A = [1,2,3,4,5,6,7,8,9,10]
    test(5, A, [3628800,1814400,1209600,907200,725760,604800,518400,453600,403200,362880], p.problem2(A))

    print("All regular test cases passed!")
    print()
    print("Begin extra credit test cases")
    print("-----------------------------")
    print("(in this section, even valid solutions may produce errors beyond failed test cases. don't worry!)")

    # Test 1
    # https://en.wikipedia.org/wiki/Empty_product
    A = [5]
    test(1, A, [1], p.problem2(A))

    # Test 2
    # If you're dividing, this should give you an error ;)
    A = [0,2,6]
    test(2, A, [12,0,0], p.problem2(A))

    print("All extra credit test cases passed! ggwp")

if __name__ == "__main__":
    main()
