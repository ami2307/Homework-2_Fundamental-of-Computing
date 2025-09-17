def longest_lines(filename):
    try:
        with open(filename) as f:
            lines = [line.rstrip('\n') for line in f]
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
        return
    if not lines:
        print([])  
        return
    max_length = max(map(len, lines))
    result = [line for line in lines if len(line) == max_length]
    print(result)

longest_lines('foo.txt')

