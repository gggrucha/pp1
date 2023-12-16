import mykeyboard
import mymath

moj_num = mykeyboard.read_number()
komp_num = mymath.generate_number()

print('Computer number: ',komp_num)
if moj_num==komp_num:
    print('you won the game!!')
else:
    print('nie udalo sie')