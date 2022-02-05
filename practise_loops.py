class Loopers():
    def __init__(self, n: int):
        self.n = n

    def __check_for_alphabetical_code(self):
        if self.n > 26:
            print("Cannot run code")
            return 

    def number_pyramid(self):
        for x in range(1, self.n+1):
            for y in range(0, x):
                print(x, end=" ")

            print()

        return

    def alphabet_pyramid_lowercase(self):
        if self.n > 26:
            print("Cannot run code")
            return 

        alphabet = 65
        for row_no in range(1, self.n+1):
            for letter in range(alphabet, alphabet+row_no):
                words = chr(letter).lower()
                print(words, end=" ")
            print()
        return 

    def printing_squares_of_numbers(self):
        for row_no in range(1, self.n+1):
            for square in range(1, row_no+1):
                print(square*square, end=" ")
            print()

        return 

    def printing_numbers_in_reverse(self):
        for row_no in range(1, self.n+1):
            for numbers in range(row_no, 0, -1):
                print(numbers, end=" ")

            print()

        return 

    def upside_down_pyramid(self):
        for row_no in range(1, self.n+1):
            for number in range(self.n-row_no+1, 0, -1):
                print(row_no, end=" ")
            
            print()

        return

    def upside_down_alphabet_pyramid(self):
        if self.n > 26:
            print("Cannot run the code")
            return 
        
        for row_no in range(1, self.n+1):
            alphabet = 65
            for letter in range(self.n - row_no+1, 0, -1):
                print(chr(alphabet), end=" ")
                alphabet = alphabet+1
    
            print()

        return 

    def upside_down_reverse_pyramid(self):
        if self.n > 26:
            print("Cannot run code")
            return 

        for row_no in range(1, self.n+1):
            for space in range(0, row_no-1):
                print(2*" ", end="")
    
            for letters in range(91-(self.n-row_no+1), 91):
                print(chr(letters), end =" ")
            print()

        return

    def full_pyramid_of_numbers(self):
        for row_no in range(0, self.n):
            if row_no >=10:
                for spaces in range(0, self.n-row_no-2):
                    print(2*" ", end ="")

                print(" ")

            else: 
                for spaces in range(0, self.n-row_no-1):
                    print(2*" ", end ="")

            for left_numbers in range(row_no, 0, -1):
                if row_no==0:
                    print(row_no)

                print(left_numbers, end=" ")

            for right_numbers in range(0, row_no+1):
                print(right_numbers, end=" ")

            print()

        return 

    




