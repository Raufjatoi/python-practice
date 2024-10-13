import sys
import random
from pyfiglet import Figlet, FigletFont

def main():
    figlet = Figlet()
    
    if len(sys.argv) == 1:
        fonts = FigletFont.getFonts()
        random_font = random.choice(fonts)
        figlet.setFont(font=random_font)
    elif len(sys.argv) == 3:
        if sys.argv[1] in ["-f", "--font"]:
            font_name = sys.argv[2]
            if font_name in FigletFont.getFonts():
                figlet.setFont(font=font_name)
            else:
                print(f"Error: '{font_name}' is not a valid font name.")
                sys.exit(1)
        else:
            print("Error: First argument must be -f or --font.")
            sys.exit(1)
    else:
        print("Usage: python figlet.py [-f | --font <font_name>]")
        sys.exit(1)

    text = input("Enter text to render: ")
    rendered_text = figlet.renderText(text)
    
    print(rendered_text)

if __name__ == "__main__":
    main()

