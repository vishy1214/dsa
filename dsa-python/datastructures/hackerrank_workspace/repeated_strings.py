def repeatedString(s, n):
    # Write your code here
    a_count_in_s = s.count('a')
    full_repeats = n // len(s)
    remaining_chars = n % len(s)
    print(f'{full_repeats} * {a_count_in_s}  + {remaining_chars}')
    total_a_count = full_repeats * a_count_in_s + s[:remaining_chars].count('a')
    print(total_a_count)

repeatedString("aba",10)