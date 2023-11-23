import os

def file_statistics(path: str):
    try:
        if not os.path.exists(path):
            raise OSError
        elif os.path.isfile(path) and not path.endswith(".txt"):
            raise ValueError
    except OSError:
        print(f"OSError: Path {path} does not exist")
        return
    except ValueError:
        print(f"ValueError: Path {path} is not a text file")
        return
    
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
        n_words = 0
        n_chars = 0
        n_digits = 0
        n_lines = len(lines) 
        for line in lines:
            line = line.replace('\r', '').replace('\n', '')
            n_words += len(line.split())
            for char in line:
                # n_chars zählt nu ned richtig
                n_chars += 1
                if char.isdigit():
                    n_digits += 1
                
    print("--------------------")
    print(f"Statistics of file {path}:")
    print(f"Number of lines: {n_lines}")
    print(f"Number of words: {n_words}")
    print(f"Number of characters: {n_chars}")
    print(f"Number of digits: {n_digits}")
    print("--------------------")
    
file_statistics('a6\Examples\ex1_1.txt')
file_statistics('a6\Examples\ex1_2.txt')
file_statistics('a6\Examples\ex1_3.txt')
file_statistics('a6\Examples\ex1_4.py')
file_statistics('a6\Examples\ex1_5.txt')
