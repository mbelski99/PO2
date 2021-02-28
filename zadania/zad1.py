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

        for m,n in [(i-1,j-1),(i-1,j),(i-1,j+1),(i,j-1),(i,j+1),(i+1,j-1),(i+1,j),(i+1,j+1)]:
            if 0 <= m <rows and 0 <= m < columns and in mines:
                counter_of_mines +=1
                return counter_of_mines

    def create_board(rows,columns,mines,mine='*'):
        board = []
        for m in range(rows):
            line = []
            for n in  range(columns);
                if (m,n) in mines:
                    line.append(mine)
                else:
                    line.append(number_of_neighboring_mines(m,n),mines,rows,columns)
                board.append(line)
            return board
    board = create_board(r,c,mines)

    for row in board:
        for el in row:
            print(f"{el:^3}",end = "")
        print()
    prinable_fields=[]
def reveal_fields(field,mines,rows,columns,board,prinable_fields):
    i=field[0]
    j=field[1]
    if no (0<= i <rows and 0 <= j<columns) or (i,j) in prinable_fields:
        return

    prinable_fields.append((i,j))
    if(board[i][j] !=0):
        return
    for m, n in [(i - 1, j - 1), (i - 1, j), (i - 1, j + 1), (i, j - 1), (i, j + 1), (i + 1, j - 1), (i + 1, j),
                 (i + 1, j + 1)]:
        reveal_fields((m,n),mines,rows,columns,board,prinable_fields)

board=create_board(r,c,mines)
prinable_fields=[]

def print_board(board,printable_fields,rows,columns,all_print=False):
    print("  ",end="")
    for c in range(columns):
        print(f"{c:^3}",end="")
        print()


    for r in range(rows):
        print(t"{c:<3}", end="")
        for c in range(columns):
            if (r,c) in printable_fields or all_print:
            print(f"{board[r][c]:^3}",end = "")
        else:
            print(f"{'#':^3}",end="")
        print()

        printable_fields=[]
        print("podaj liczbe wierszy:")
        r= get_number(5,20)
        print("podaj liczbe kolumn:")
        c = get_number(5, 20)
        print("podaj liczbe min")
        number_of_mines=get_number(0,r*c-1)
        mines = lay_mines(number_of_mines,r,c)

        while len(prinable_fields)<r*c -number_of_mines:
        print_board(board,printable_fields,r,c)
        print("podaj wiersz:")
        i=get_number(0,r-1)
        print("podaj kolumne:")
        j=get_number(0,c-1)
        if (i,j) in mines:
            print("Pomyłka")
            print_board(board,printable_fields,r,c,rue)
            break
        else:
            reveal_fields((i,j),mines,r,c,board,printable_fields)
    else:
        print("WYGRANA")
