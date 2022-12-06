from game import generate_game

def main():
  # initialize and run game
  sudoku = generate_game()
  sudoku.loop()

if __name__ == "__main__":
  main()
