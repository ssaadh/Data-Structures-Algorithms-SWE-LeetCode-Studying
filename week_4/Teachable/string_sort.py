def stringSort(s):
    #runtime: O(nlgn)
    #space: O(N)
    #as array O(1)
  sortedStr = sorted(s.replace(" ",""))
  return "".join(sortedStr)

def stringSortCountsArr(s):
    #alphabet: R
    #runtime: O(N + R)
    #space: O(N)
    #as array: O(R)
    alphabetSize = 26
    counts = [0]*alphabetSize
    for c in s.replace(" ",""):
        counts[ord(c) - ord('a')] += 1
    newStr = []
    for i,numLetters in enumerate(counts):
        newStr.append(chr(i+ord('a'))*numLetters)

    return "".join(newStr)

def stringSortMultiPass(s):
    alphabetSize = 26
    s = list(s.replace(" ",""))
    swap_index = 0
    for i in range(alphabetSize):
        curLetter = chr(i+ord('a'))
        for j,c in enumerate(s):
            if c == curLetter:
                s[swap_index], s[j] = s[j], s[swap_index]
                swap_index += 1
    return "".join(s)

if __name__ == '__main__':
    #alphabet of size 26 - aka constant
    s = "the quick brown fox jumps over the lazy dog"
    # "abcde...z"
    print(stringSort(s))

    s = "the quick brown fox jumps over the lazy dog"
    print(stringSortCountsArr(s))


    s = "the quick brown fox jumps over the lazy dog"
    print(stringSortMultiPass(s))
    # s = "abc deeek hrown fox jumps ovir thu ltzy qog"

    # counts =
    #  a,b,c,d,e,...,z
    # [1,1,1,1,3,...,1]
    #
    #
    # "abcdeee....z"
