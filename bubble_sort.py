data = [4,3,1,9,6,5,7,29,2]

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

bubble_sort(data)
