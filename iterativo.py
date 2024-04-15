def main(num_list):
    for x in num_list:
        if(x % 2 == 0):
            print(f"{x} é par")
        else:
            print(f"{x} é ímpar")
    
main([1,2,3])