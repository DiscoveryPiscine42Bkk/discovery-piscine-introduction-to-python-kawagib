import sys

def main():
    if len(sys.argv) == 1:
        print("none")
        return
    
    for word in sys.argv[1:]:
        if word.endswith("ism"):
            continue
        print(word + "ism")

if __name__ == "__main__":
    main()