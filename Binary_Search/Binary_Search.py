# @Author: Wang
# @Date  : 2018/9/23

def binary_search(list,item):
    low = 0
    high = len(list) - 1

    while low < high:
        mid = int((low+high)/2)
        guess = list[mid]
        # print('guess:%d,item:%d,low:%d,high:%d' %(guess,item,low,high))
        if guess < item:
            low = mid + 1   #   猜测的比真实值小，则下面菜的数不能比本次的值更低
        elif guess > item:
            high = mid - 1
        else:
            return mid
    return None

my_list = [1,3,5,7,9]
print(binary_search(my_list,5))
print(binary_search(my_list,-1))