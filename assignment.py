def bubble_sort(data):
    n = len(data)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                temp = data[j]
                data[j] = data[j + 1]
                data[j + 1] = temp
                swapped = True
        if swapped == False:
            break
    return data


def bubble_sort_trace(data):
    trace = []
    n = len(data)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                temp = data[j]
                data[j] = data[j + 1]
                data[j + 1] = temp
                swapped = True
        if swapped == False:
            break
        trace.append(data.copy())
    return trace


def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data


def insertion_sort_trace(data):
    trace = []
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
        trace.append(data.copy())
    return trace


def rank_students(records):
    for i in range(1, len(records)):
        key = records[i]
        j = i - 1
        while j >= 0 and records[j][1] < key[1]:
            records[j + 1] = records[j]
            j -= 1
        records[j + 1] = key
    return records
