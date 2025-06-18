def main():
    original_array = [2, 8, 9, 48, 8, 22, -12, 2]

    processed = [x + 2 for x in original_array if x > 5]

    no_deplicates = list(set(processed))

    print("Original array:", original_array)
    print(no_deplicates)

if __name__ == "__main__":
    main()