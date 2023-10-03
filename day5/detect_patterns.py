def detect_pattern(str1, str2):
    # check for equility
    if str1 == str2:
        return True
    # check for length
    if len(str1) != len(str2):
        return False
    else:
        # check if a letter is repeated, if not repeated in both strings, there is a pattern
        seen_letters = []
        for i in range(len(str1)):
            if str1[i] in seen_letters:
                return True
            seen_letters.append(str1[i])
            if str2[i] in seen_letters:
                return True
            seen_letters.append(str2[i])
        return False

print(detect_pattern("", "")) #true
print(detect_pattern("a", "a")) #true
print(detect_pattern("x", "y")) #true
print(detect_pattern("ab", "xy")) #true
print(detect_pattern("aba", "xyz")) #false
print(detect_pattern("---", "xyz")) #false
print(detect_pattern("---", "aaa")) #true ****
print(detect_pattern("xyzxyz", "toetoe")) #true ****
print(detect_pattern("xyzxyz", "toetoa")) #false 
print(detect_pattern("aaabbbcccd", "eeefffgggz")) #true ****
print(detect_pattern("cbacbacba", "xyzxyzxyz")) #true ****
print(detect_pattern("abcdefghijk", "lmnopqrstuv")) #true
print(detect_pattern("asasasasas", "xxxxxyyyyy")) #false
print(detect_pattern("ascneencsa", "aeiouaeiou")) #false
print(detect_pattern("aaasssiiii", "gggdddfffh")) #false