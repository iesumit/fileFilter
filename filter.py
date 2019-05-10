
def read_large_file(file_handler, block_size=10000):
    block = []
    for line in file_handler:
        block.append(line)
        if len(block) == block_size:
            yield block
            block = []            
    # yield the last block
    if block:
        yield block

with open(path) as file_handler:
    for block in read_large_file(file_handler):
        print(block)
