def get_number(a,b):
    while True:
    number = int(input(f"Podaj liczbę z zakresu {a} do {b}"))
    if number >= a and number <=b: #a<=number <= b
        return number
    else:
        print("Błąd! Przekroczony zakres! Podaj liczbę ponownie!")

    print(get_number(1,10))

    def lay_mines(number_of_mines,rows,columns):

        mines=set()
        while len(mines) < number_of_mines:
            m= random.radint(0,rows-1)
            n= random.randrange(columns)
            mines.add((m,n))
        return mines

    r=10
    c=10
    number_of_mines = get_number(0,r*c-1)
    mines = lay_mines(number_of_mines,r,10)
    print(mines)

    def number_of_neighboring_mines(field,mines,rows,columns):
        counter_of_mines=0
        i = field[0]
        j = field[1]

        for m,n in [(i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]
            if 0 <= m <rows and 0 <= m < columns and in mines:
                counter_of_mines +=1
                return counter_of_mines

    def create_board(rows,columns,mines,mine='*'):