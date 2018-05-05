# Python program to find the symmentric diference betweens sets
#  The term symmetric difference indicates those values
#  that exist in either  or  but do not exist in both.


def symmentric(seta, setb):
    return seta.symmetric_difference(setb)


if __name__ == '__main__':
    a, b = [map(int, input().split()) for _ in range(4)][1::2]
    sortedset = sorted(symmentric(set(a),set(b)),key=None,reverse=False)
    for item in sortedset:
        print(item)
