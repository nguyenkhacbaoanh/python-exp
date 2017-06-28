import random
data = random.sample(range(100),10)

def bubble_sort(list):

    sort_init = True

    while sort_init:

        sort_init = False

        for i in range(len(data)-1):

            if data[i] > data[i+1]:
                x = data[i]
                data[i] = data[i+1]
                data[i+1] = x
                sort_init = True

    return print(list)
print(data)
bubble_sort(data)
