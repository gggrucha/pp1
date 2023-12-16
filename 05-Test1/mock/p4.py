def f(card_number):
    result = ''
    for i in range(len(card_number)):
        if i in range(0,2) or i in range(12,16):
            result+=card_number[i]
        elif i in range(2,13):
            result+='*'
    return result

if __name__ == '__main__':  
    print(f('5290312400019022'))
