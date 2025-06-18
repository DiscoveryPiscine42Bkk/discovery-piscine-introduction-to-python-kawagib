import sys

def main():
    if len(sys.argv) != 2:
        print("none")
        return
    
    input_string = sys.argv[1]
    found = False

    for char in input_string:
        if char == 'z' :
            print('z', end='')
            found = True

        if not found:
            print("none")

if __name__ == "__main__":
        main()