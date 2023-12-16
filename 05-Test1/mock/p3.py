def f(name):
    result = ''
    acro = name.split(' ') #['Internet', 'of', 'Things']
    for word in acro:
        result+= word[0] #'IoT'
    return result

if __name__ == '__main__':
    print(f('Internet of Things'))
    print(f('For Your Information'))
    print(f('Python'))