# Strontium 2019
# ConcatenatingOfWords: Concatenate the given words in such a way as to obtain a single word with the longest possible substring composed of one particular letter.
def concatenatingOfWords(words):
    res = 0
    pure = [0 for i in range(26)]
    pure_index = set()
    for j in range(len(words)):
        w = words[j]
        temp = 1
        for i in range(1, len(w)):
            if w[i]==w[i-1]:
                temp += 1
            else:
                res = max(res, temp)
                temp = 1
        if temp==len(w):
            pure[ord(w[0])-97] += temp
            pure_index.add(j)
        res = max(res, temp)    
    # [3,5,8,2]->length=5 at position 3, length=2 at position 8
    rec_head = [[-1,0,-1,0] for i in range(26)]
    rec_tail = [[-1,0,-1,0] for i in range(26)]
    for i in range(len(words)):
        if i not in pure_index:
            w = words[i]
            head, tail = w[0], w[-1]
            hl, tl = 1, 1
            hi, ti = ord(head)-97, ord(tail)-97
            for j in range(1, len(w)):
                if w[j]==head:
                    hl += 1
                else:
                    if hl > rec_head[hi][1]:
                        rec_head[hi] = [i, hl, rec_head[hi][0], rec_head[hi][1]]
                    elif hl > rec_head[hi][3]:
                        rec_head[hi] = [rec_head[hi][0], rec_head[hi][1], i, hl]
                    break
            for j in range(len(w)-2, -1, -1):
                if w[j]==tail:
                    tl += 1
                else:
                    if tl > rec_tail[ti][1]:
                        rec_tail[ti] = [i, tl, rec_tail[ti][0], rec_tail[ti][1]]
                    elif tl > rec_tail[ti][3]:
                        rec_tail[ti] = [rec_tail[ti][0], rec_tail[ti][1], i, tl]
                    break
    for i in range(26):
        head, tail = rec_head[i], rec_tail[i]
        temp = 0
        if head[0]==tail[0]:
            temp = max(head[1]+tail[3], head[3]+tail[1]) + pure[i]
        else:
            temp = head[1] + tail[1] + pure[i]
        res = max(res, temp)
    return res
    pass

# ["aabb", "aaaa", "bbab"] = 6
print("[""aabb"", ""aaaa"", ""bbab""], the length of the longest substring of word is", str(concatenatingOfWords(["aabb", "aaaa", "bbab"])))
# ["xxbxx", "xbx", "x"] = 4
print("[""xxbxx"", ""xbx"", ""x""], the length of the longest substring of word is", str(concatenatingOfWords(["xxbxx", "xbx", "x"])))
# ["dd", "bb", "cc", "dd"] = 4
print("[""dd"", ""bb"", ""cc"", ""dd""], the length of the longest substring of word is", str(concatenatingOfWords(["dd", "bb", "cc", "dd"])))
