import sys
from checkmate import checkmate

def read_board_from_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
        return content
    except:
        return None

def main():
    for filename in sys.argv[1:]:
        board = read_board_from_file(filename)
        if board is None:
            print("Error")
            continue
        checkmate(board)

if __name__ == "__main__":
    main()