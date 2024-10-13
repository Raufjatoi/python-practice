import emoji

def emojize_text(input_text):
    return emoji.emojize(input_text, use_aliases=True)

def main():
    user_input = input('Input: ')
    
    emojized_output = emojize_text(user_input)
    
    print('Output: ', emojized_output)

if __name__ == "__main__":
    main()
