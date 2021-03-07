puzzle = 'WAQHGTTWEECBMIVQQELSAPXWKWIIILLDELFXPIPVPONDTMVAMNOEDSOYQGOBLGQCKGMMCTYCSLOACUZMXVDMGSXCYZUUIUNIXFNU'
words = 'UNIX CALPOLY GCC SLO CPE COMPILE VIM TEST'

def format_puzzle(puzzle): #returns list of strings, each string is a row of the puzzle
   characters = [char for char in puzzle]
   formatted_puzzle = []

   for i in range(0, 100, 10):
      line = [characters[i + j] for j in range(10)]
      formatted_puzzle.append(''.join(line))

   return formatted_puzzle

def format_words(words): #returns list of words as strings
   return words.split()

def find_words(puzzle, words): #gets list of tuples with location of words
   locations = []
   for word in words:
      if search_rows(puzzle, word):
         locations.append(search_rows(puzzle, word))
      elif search_columns(puzzle, word):
         locations.append(search_columns(puzzle, word))
      elif search_diagonals(puzzle, word):
         locations.append(search_diagonals(puzzle, word))
      else:
         locations.append(None)
   return locations

def search_rows(puzzle, word): #searches forwards and backwards for a word
   for i in range(len(puzzle)):
      if puzzle[i].find(word) >= 0:
         location = (i, puzzle[i].find(word), '(FORWARD)')
         return location
      elif puzzle[i].find(reverse_word(word)) >= 0:
         location = (i, puzzle[i].find(reverse_word(word))+len(word)-1, '(BACKWARD)')
         return location
   return None

def reverse_word(word): #reverses a word
   return ''.join([word[i] for i in range(len(word)-1, -1, -1)])

def search_columns(puzzle, word): #searches up and down for a word
   col = 0
   for i in range(len(puzzle)):
      column = []
      for j in range(len(puzzle)):
         column.append(puzzle[j][i])
      if ''.join(column).find(word) >= 0:
         location = (''.join(column).find(word), col, '(DOWN)')
         return location
      elif ''.join(column).find(reverse_word(word)) >= 0:
         location = (''.join(column).find(reverse_word(word))+len(word)-1, col, '(UP)')
         return location
      col += 1
   return None

def search_diagonals(puzzle, word):
   #found = False
   for i in range(len(puzzle)): #search every row
      for j in range(len(puzzle[i])): #search every character in row
         if puzzle[i][j] == word[0]:
            if search_characters(puzzle, word, i, j) == True:
               location = (i, j, '(DIAGONAL)')
               return location
   return None

def search_characters(puzzle, word, row, col):
   for k in range(1, len(word)):
      if (row + k) < 10 and (col + k) < 10:
         if word[k] != puzzle[row+k][col+k]:
            return False
      else:
         return False
   return True

