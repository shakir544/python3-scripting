# python example of map and lambda

cube = lambda x : x **3


# one of the many ways to write fibonacii
# Method 1
def fibonacci(n):
    list = [0,1]
    for i in range(2,n):
        list.append(list[i-2] + list[i-1])
    return list[0:n]


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))