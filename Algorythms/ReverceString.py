#переворот [::-1]
string = "Hello!"
def reverse_string(s):
    chars = list(s)
    for i in range(len(s) // 2):
        temp = chars[i]
        chars[i] = chars[len(s) - i - 1]
        chars[len(s) - i - 1] = temp
    return ''.join(chars)
reverse_string(string)