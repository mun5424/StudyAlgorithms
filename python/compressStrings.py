# Implement a method to perform basic string compression using the counts of repeated characters. 
# For example, the string aabcccccaaa would become a2blc5a3

def compressString(word):
    char_count = 1
    compressed = []
    for i in range(0 , len(word)-1): 
        if word[i] == word[i + 1]:
            char_count += 1
        else: 
            compressed.append(word[i])
            compressed.append(str(char_count))
            char_count = 1
    if char_count >= 1:
        compressed.append(word[i+1])
        compressed.append(str(char_count))
    return ''.join(compressed)
        

print(compressString('aaaacdddd'))