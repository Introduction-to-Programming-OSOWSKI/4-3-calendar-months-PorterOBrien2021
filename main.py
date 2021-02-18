def calendar(x):
    for i in range (0, 12):
        if months[i] == x:
            return i + 1
    return x + " is not a month"

months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]

print(calendar("march"))