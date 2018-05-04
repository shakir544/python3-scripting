# Sample python program to calculate the average of numbers in set

# Function to calculate the average
def average(array):
    dis = set(array)
    return sum(dis)/len(dis)


if __name__ == '__main__':
    N = int(input())
    array = list(map(int,input().split()))
    print(average(array))


