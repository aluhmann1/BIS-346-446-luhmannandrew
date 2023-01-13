values = [list(range(0, 10)), 
          list(range(10, 20)), 
          list(range(20, 30)), 
          list(range(30, 40)), 
          list(range(40, 50)), ]

def display_table(twoD_list, column_width):
    
    # indent titles by the width of max row index number
    indent = len(str(len(twoD_list)))
    print(f'{"":{indent}}', end='')

    for col in range(len(twoD_list[0])):
        print(f'{col:>{column_width}}', end='')

    print()

    for i, row in enumerate(twoD_list):
        print(f'{i:>{indent}}', end='')

        for value in row:
            print(f'{value:>{column_width}}', end='')

        print()
          
display_table(values, 5)