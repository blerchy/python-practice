#
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
#
# Bonus: Can you do this in one pass?
#

def problem1(A, k):

    # your solution here

    for i in range(0, len(A)):
        for j in range(i-1, -1, -1):
            if (A[i] + A[j] == k):
                return True

    return False

if __name__ == "__main__":

    A = [1,2,3]
    k = 3

    print(problem1(A,k))
