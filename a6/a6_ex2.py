import os


def chunks(path: str, size: int, **kwargs):
    try:
        if size < 1:
            raise ValueError("Size must be greater than or equal to 1.")
        if not os.path.isfile(path):
            raise ValueError(f"{path} is not a file.")

    except ValueError as err:
        print(err)
        return
        
    with open(path, **kwargs) as file:
        while True:
            chunk = file.read(size)

            # check if chunk is empty
            if not chunk:
                break

            yield chunk


for i, c in enumerate(chunks("a6\Examples\ex2_example.txt", 0, mode="rb")):
    print(f"Chunk {i} = {c}")
for i, c in enumerate(chunks("a6\Examples\ex2_example.tt", 25, mode="rb")):
    print(f"Chunk {i} = {c}")
for i, c in enumerate(chunks("a6\Examples\ex2_example.txt", 25, mode="rb")):
    print(f"Chunk {i} = {c}")
