import time

def does_name_exist(first_names, last_names, full_name):
    start = time.perf_counter()
    for fname in first_names:
        for lname in last_names:
            if fname + " " + lname == full_name:
                end = time.perf_counter()
                print(end - start)
                return True
    end = time.perf_counter()
    print(end - start)

    return False
