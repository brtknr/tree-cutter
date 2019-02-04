import sys


def format(func):
    def wrapper(a, expected):
        answer = func(a)
        print(
            '\033[1;32;40m' if answer == expected else '\033[1;31;40m',
            a, '->', answer, '\033[0m \n'
        )
        if answer != expected:
            sys.exit(1)
    return wrapper


@format
def solve(a):
    answer = len(a)
    if len(a) > 1:
        asc_succ = {}
        for i in reversed(range(len(a) - 1)):
            asc_succ[i] = (
                a[i] <= a[i + 1] and
                asc_succ.setdefault(i + 1, True)
            )
        answer = 0
        for i in range(len(a)):
            if i == 0:
                if asc_succ.setdefault(i + 1, True):
                    answer += 1
            elif i + 1 == len(a):
                answer += 1
            else:
                if a[i - 1] <= a[i + 1] and asc_succ.setdefault(i + 1, True):
                    answer += 1
                if a[i - 1] > a[i]:
                    break
    return answer


if __name__ == '__main__':
    solve([], 0)
    solve([3], 1)
    solve([3, 2], 2)
    solve([2, 3, 4, 2, 5], 1)
    solve([3, 4, 5, 4], 2)
    solve([4, 5, 2, 3, 4], 0)
    solve([1, 5, 8, 11, 19], 5)
    solve([1, 2, 3, 4, 3, 4, 4, 5, 6], 2)
    solve(range(1000000), 1000000)
