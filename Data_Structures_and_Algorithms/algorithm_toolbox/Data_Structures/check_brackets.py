# python3

#Input: contains one string S whcih consists of big and small latin letters, digits, puncutation marks and brackets from
# the set []{}()

#Output: If brackets are all used (closed correctly) output success 'Success'
#        Index of first unmatched closing bracket
#        If no unmatched closing brackets, output the 1-based index of the first unmatched opening bracket
def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            opening_brackets_stack.append([i,next])
            pass
        if next in ")]}":
            if len(opening_brackets_stack) == 0:
                return i
            top = opening_brackets_stack.pop()
            if (next == ']' and top[1] != '[') or (next == ')' and top[1] != '(') or (next == '}' and top[1] != '{'):
                return i
            pass
    if len(opening_brackets_stack) != 0:
        return opening_brackets_stack[0][0]
    return 'Success'

def main():
    text = input()
    mismatch = find_mismatch(text)
    print(mismatch)

if __name__ == "__main__":
    main()
