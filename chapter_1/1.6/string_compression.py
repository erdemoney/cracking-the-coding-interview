import sys            
# question:
#   Implement an method to perform basic string compression using the counts of
#   repeated characters. For example, the sting "aabcccccaaa" would become
#   "a2b1c5a3". If the "compressed" string would not become smaller than the
#   original string, your method should return the original string. You can
#   assume the string has only uppercase and lowercase letters.
#
# concept:
#   count duplicate characters and concatenate compressed notation
#   to return string

def stringCompression(input: str) -> str:
    if len(input) == 0:
        return input
    compressed = '' 
    prev_char = input[0]
    count = 0
    for i in range(len(input)):
        c = input[i]
        # if last char add to compressed string 
        if i == len(input)-1:
            if(c == prev_char):
                compressed += prev_char +str(count+1)
                continue
            compressed += c + str(1)

        # if char is different than last add compressed count for last run
        # and reset length
        if c != prev_char:
            compressed += prev_char + str(count)
            prev_char = c
            count = 1
            continue
        # if char is same as last inc len of run
        count += 1
    if len(compressed) < len(input):
        return compressed
    return input

def main() -> int:
    print(stringCompression(sys.argv[1]))
    return 0

sys.exit(main())
