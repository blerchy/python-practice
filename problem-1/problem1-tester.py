import problem1 as p

def test(num, A, k, expected, actual):
    if expected == actual:
        print("Test #" + str(num) + " passed.")
    else:
        print("TEST #" + str(num) + " FAILED!")
        print("For k = " + str(k) + " and A = " + str(A) + ", expected " + str(expected) + " but got " + str(actual) + ".")
        exit(0)

def main():
    # Test 1
    A = [10,15,3,7]
    k = 17
    test(1, A, k, True, p.problem1(A,k))

    # Test 2
    A = [0]
    k = 0
    test(2, A, k, False, p.problem1(A,k))

    # Test 3
    A = [0,0]
    k = 0
    test(3, A, k, True, p.problem1(A,k))

    # Test 4
    A = [1,2,3,4]
    k = 1
    test(4, A, k, False, p.problem1(A,k))

    # Test 5
    k = 2
    test(5, A, k, False, p.problem1(A,k))

    # Test 6
    k = 3
    test(6, A, k, True, p.problem1(A,k))

    # Test 7
    k = 4
    test(7, A, k, True, p.problem1(A,k))

    # Test 8
    k = 5
    test(8, A, k, True, p.problem1(A,k))

    # Test 9
    k = 6
    test(9, A, k, True, p.problem1(A,k))

    # Test 10
    k = 7
    test(10, A, k, True, p.problem1(A,k))

    # Test 11
    k = 8
    test(11, A, k, False, p.problem1(A,k))

    # Test 12
    A = [1, -3, 4]
    k = 1
    test(12, A, k, True, p.problem1(A,k))

    # Test 13
    k = -2
    test(13, A, k, True, p.problem1(A,k))

    print("All tests passed!")

if __name__ == "__main__":
    main()