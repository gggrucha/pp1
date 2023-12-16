def f(detector):
    lenght = 0
    for char in detector:
        if lenght >= 3:
            return True
        if char=='+':
            lenght+=1
        elif char == '-':
            lenght-=1
    return False

print(
f("+-+++-+---"),
f("+-+-+-+-"),
f("+-++-+--"),
f("+-++-++-+---") 
)