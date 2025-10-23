def count_case_letters(s):
    upper_count = sum(1 for c in s if c.isupper())
    lower_count = sum(1 for c in s if c.islower())
    return upper_count, lower_count

sample_string = "Hello World!"

upper, lower = count_case_letters(sample_string)
print(f"upper {upper}", f"lower {lower}")
