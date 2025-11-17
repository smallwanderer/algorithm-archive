from implementation.List import List

list = List()
while True:
  command = input("[Menu] i-input, d-delete, r-replace, p-print, l-list, s-save, q-quit => ")

  if command == 'i':
    pos = int(input("input position => "))
    str = input("input string => ")
    list.insert(pos, str)

  elif command == 'd':
    pos = int(input("delete position => "))
    list.delete(pos)

  elif command == 'r':
    pos = int(input("replace position => "))
    str = input("replace string => ")
    list.replace(pos, str)

  elif command == 'p':
    print("Line Editor")
    for line in range(list.size):
      print(f"{line} {list.getEntry(line)}")
    print()

  elif command == 'q':
    exit()

  elif command == 'l':
    filename = "implementation/test.txt"
    infile = open(filename, "r", encoding='CP949')
    lines = infile.readlines()
    for line in lines:
      list.insert(list.size, line.rstrip('\n'))
    infile.close()

  elif command == 's':
    filename = "implementation/test.txt"
    outfile = open(filename, "w", encoding='CP949')
    len = list.size
    for i in range(len):
      outfile.write(list.getEntry(i)+'\n')
    outfile.close()