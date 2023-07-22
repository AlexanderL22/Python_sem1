numb = int(input("Введите количество рядов: "))
spaces = numb-1
stars = 1
for i in range(numb):
    print(
              (' '*spaces) +
              ('*'*stars) 
          )
    stars += 2
    spaces -= 1