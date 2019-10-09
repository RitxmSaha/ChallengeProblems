def num_after_point(x):
    s = str(x)
    print(list(s))
    if not '.' in s:
        return 0
    return len(s) - s.index('.') - 1

print(num_after_point(1/2))