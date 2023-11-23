import os

def chunks(path: str, size: int, **kwargs):
    if size < 1:
        raise ValueError("Size must be greater than or equal to 1.")

    try:
        with open(path, **kwargs) as file:

            if not os.path.isfile(path):
                raise ValueError(f"{path} is not a file.")

            while True:
                chunk = file.read(size)

                if not chunk:
                    break

                yield chunk

    except FileNotFoundError:
        raise ValueError(f"File not found: {path}")
    
    
for i, c in enumerate(chunks("a6\Examples\ex2_example.txt", 25, mode="rb")):
    print(f"Chunk {i} = {c}")