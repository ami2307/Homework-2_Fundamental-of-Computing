def longest_lines(filename):
    with open(filename) as f:
        lines = [line.rstrip('\n') for line in f]
    
    if not lines:
        return []

    max_length = max(map(len, lines))
    return [line for line in lines if len(line) == max_length]
