# number of alphabets : 26
# 'aa' -> 1 * (27 ** 1) + 1
# n보다 작은 크기의 ban을 찾고, n에서 해당 값 빼고, 거기서 26진수 변환

base26_dict = {chr(96+n): n for n in range(1, 27)}
BASE = 26

def base_to_num(char):
    length = len(char)
    result = 0
    for i in range(length):
        power = length-i-1
        result += base26_dict[char[i]] * (BASE ** power)
    return result
#print(base_to_num('az'))

def num_to_base(num):
    result = ''
    while num > 0:
        char = chr(97+((num-1) % 26))
        result = char + result
        num = (num-1) // 26
    return result
#print(num_to_base(26))

def solution(n, bans):
    bans = list(map(base_to_num, bans))
    bans.sort()
    for b in bans:
        if b <= n: n += 1
    return num_to_base(n)