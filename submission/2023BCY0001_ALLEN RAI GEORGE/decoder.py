from key import *

def decrypt(text: str):
    
    try:
        text = list(text)
        for i in range(len(text)):
            key_element = int(KEY[i%LENGTH])
            text[i] = chr(ord(text[i]) + (key_element if not ((i+1)%2) and not (key_element % 2) else -key_element))
            
    except Exception as e:
        print(f"Error: {e}")
        print(f"This error was given by the encrypted text: {text!r}")
        
    return ''.join(text)


def main():
    text = "qG=5}9SK"
    print(decrypt(text))



if __name__ == "__main__":
    main()