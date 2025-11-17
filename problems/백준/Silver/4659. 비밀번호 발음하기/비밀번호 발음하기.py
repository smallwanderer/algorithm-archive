# 모음(a,e,i,o,u) 하나를 반드시 포함하여야 한다.
# 모음이 3개 혹은 자음이 3개 연속으로 오면 안 된다.
# 같은 글자가 연속적으로 두번 오면 안되나, ee 와 oo는 허용한다.
import sys

vowels = {'a', 'e', 'i', 'o', 'u'}

while True:
  word = sys.stdin.readline().strip()
  if word == 'end':
    break

  is_vowel = False
  is_triple = False
  triple_check = {}
  is_double = False
  double_check = None

  for letter in word:

    # double check
    if letter == double_check and letter not in {'e', 'o'}:
      is_double = True
      break
    double_check = letter

    # vowel check
    if letter in vowels:
      is_vowel = True

    # Triple check
    if len(triple_check) == 0:
      if letter in vowels:
        triple_check['vowel'] = 1
      else:
        triple_check['const'] = 1
    else:
      if letter in vowels:
        if 'vowel' in triple_check.keys():
          triple_check['vowel'] += 1
          if triple_check['vowel'] == 3:
            is_triple = True
            break
        else:
          triple_check.clear()
          triple_check['vowel'] = 1
      else:
        if 'const' in triple_check.keys():
          triple_check['const'] += 1
          if triple_check['const'] == 3:
            is_triple = True
            break
        else:
          triple_check.clear()
          triple_check['const'] = 1

  if not is_triple and not is_double and is_vowel:
    print(f"<{word}> is acceptable.")
  else:
    print(f"<{word}> is not acceptable.")




