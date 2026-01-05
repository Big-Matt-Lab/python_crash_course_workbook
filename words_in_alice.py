from pathlib import Path

def count_words(path):
    """
    Counts words in a text file
    
    Arguments:
        path (Path): The path object to the text file.
    
    Returns:
        int: The number of words in the file, or None if the file is not found.
    """

    try: # error handling if file doesn't exist
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        print(f"Sorry, the file {path} does not exist.")
        return None
    else:
        print(contents)
        # Count the number of words in the text file
        words = contents.split()
        num_words = len(words)
        return num_words

if __name__ == "__main__":
    path = Path('alice.txt')
    word_count = count_words(path)
    if word_count is not None:
        print(f"The file {path} has approximately {word_count} words.")
    
# EOF
