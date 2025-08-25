def count_long_lines(filename: str) -> int:
    count = 0
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            words = line.split()
            if len(words) > 5:
                count += 1
    return count


# Shembull përdorimi
file_name = "test.txt"   # supozojmë që ky ekziston
result = count_long_lines(file_name)
print(f"Numri i rreshtave me më shumë se 5 fjalë: {result}")
