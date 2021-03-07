from funcs import *

def main():
   puzzle = input('LETTERS IN WORD SEARCH (LEFT TO RIGHT, TOP TO BOTTOM):\n')
   words = input('WORDS TO FIND:\n')
   formatted_puzzle = format_puzzle(puzzle)
   formatted_words = format_words(words)

   print('Puzzle:\n')
   for i in range(len(formatted_puzzle)):
      print(formatted_puzzle[i])
   print('')

   locations = find_words(formatted_puzzle, formatted_words)

   for i in range(len(formatted_words)):
      if locations[i] == None:
         print(formatted_words[i] + ': ' + 'word not found')
      else:
         word_c = formatted_words[i] + ':'
         direction = locations[i][2]
         row_num = locations[i][0]
         col_num = locations[i][1]
         print(word_c, direction, 'row:', row_num, 'column:', col_num)

if __name__ == '__main__':
   main()


