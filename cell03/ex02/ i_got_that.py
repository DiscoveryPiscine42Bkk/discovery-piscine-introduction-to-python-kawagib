def main():
    first_prompt = "What you gotta say? : "
    next_prompt = "I got that! Anything else? : "

    user_input = input(first_prompt)

    while user_input != "STOP" :
        user_input = input(next_prompt)

if __name__ == "__main__":
    main()