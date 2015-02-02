__author__ = 'amir'

n = 0


def calculateSum(n):
    sum = 0
    for i in range(n):
        sum += 3 ** i
    return sum


def main():
    for m in range(10):
        global n
        n = 0
        val = 2 ** m
        f(val)
        if n == calculateSum(m):
            print("Pass")
            print(n)
        else:
            print("fail")


def printCount(str):
    global n
    n += 1
    # print("blarg", n)


def f(n):
    if n > 1:
        printCount("blarg")
        f(n / 2)
        f(n / 2)
        f(n / 2)


if __name__ == '__main__':
    main()