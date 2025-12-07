def can_become_empty(s):
    def is_empty(substring):
        if not substring:
            return True
        return False
    for i in range(len(s)):
        substring = s[:i] + s[i+1:]
        if is_empty(substring) or can_become_empty(substring):
            return True
    return False

input_string = "abcde"
result = can_become_empty(input_string)
if result:
    print(f'The string "{input_string}" can become empty by recursive deletion.')
else:
    print(f'The string "{input_string}" cannot become empty by recursive deletion.')
