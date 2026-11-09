def solve(columns):
    # TODO: Return the columns whose lowercase name contains a leakage keyword.
    suspeitos  = ['target', 'label', 'future', 'outcome', 'post_']

    result = []

    for column in columns:
        name = column.lower()

        if any(word in name for word in suspeitos):
            result.append(column)
    return result
