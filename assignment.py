# Do NOT use sorted() or .sort() - write the algorithms yourself.

# Exercise 1
def bubble_sort(data):
    n = len(data)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped:
            break
    return data

# Exercise 2
def bubble_sort_trace(data):
    trace = []
    n = len(data)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swapped = True
        if not swapped:
            break
        trace.append(data.copy())
    return trace

# Exercise 3
def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key
    return data

# Exercise 4
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

# Exercise 5
def rank_students(records):
    for i in range(1, len(records)):
        key = records[i]
        j = i - 1
        while j >= 0 and records[j][1] < key[1]:
            records[j + 1] = records[j]
            j -= 1
        records[j + 1] = key
    return records
