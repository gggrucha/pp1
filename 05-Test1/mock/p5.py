def f(binary_number):
    for char in binary_number:
        if char == '0' or char == '1':
            continue
        else:
            return False
    return True
