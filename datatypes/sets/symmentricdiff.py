# Python program to find the symmentric diference betweens sets
#the term symmetric difference indicates those values that exist in either  or  but do not exist in both.


def symmentric(set_a, set_b):
    return (set_a-set_b).union(set_b -set_a)


if __name__ == '__main___':
    N = int(input())
    N_set = set(map(int,input().split()))
    M = int(input())
    M_set = set(map(int,input().split()))
    symmentric(N_set,M_set)

