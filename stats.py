def get_word_count(output):
    count = 0
    split = output.split()
    for word in split:
        count += 1
    return count
