import sys
system = "start"
while system == "start":
    print("Wpisz liczbę do konwersji & Informację o systemie '10' lub '2' ")
    converted_number, bin_dec = map(int,sys.stdin.readline().split()) #wpisujemy jaki system "10" czy "2"
    system = bin_dec
    while system == 2: #działamy w systemie "2"
        binary_to_string = str(converted_number) #"converted_number" zamieniamy na typ string
        temporary = binary_to_string
        new_number = 0
        power = 0
        while len(temporary) > 0:
            bit = int(temporary[-1]) #konwersja binary string na integer
            new_number = new_number + bit * 2 ** power #wynik wyliczeń
            temporary = temporary[:-1] #this steps to the next item in the string.
            power += 1 #zwiększa wartość zmiennej power o jeden do końca pętli
            system = "start"
        print(new_number)

    while system == 10: #działamy w systemie "10"
        new_int = int(converted_number) #deklaracja nowej zmiennej typu int
        binary_to_string = ''
        while new_int > 0:
            binary_to_string = str(new_int % 2) + binary_to_string
            new_int //= 2 #pętla dzielenia
            system = "start"
        print(binary_to_string)
    system = "start" # loops all program.
