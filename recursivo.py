def even_or_odd(x, num_list):
    if x < len(num_list):
        if num_list[x] % 2 == 0:
            print(str(num_list[x]) + " é par")
        else:
            print(str(num_list[x]) + " é impar")
        even_or_odd(x+1, num_list)

even_or_odd(0, [1, 2, 3, 4, 5])  
