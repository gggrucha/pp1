def f(sentence):
    new_sentence = ''
    for char in sentence:
        if char != ' ':
            new_sentence+=char
    return new_sentence

print(f('lola lol'),f('gggg s'))