# The Fellowship of the Code
# PartialSort: Given a string and an integer K, return the lexicographically minimum string that can be achieved by applying at most K swaps of adjacent letters.
import string
from bisect import bisect_left
from collections import namedtuple

MAX_N = 100000
NULL_CHAR = '-'

class IndexEntry:
    def __init__(self):
        self.index_list = []
        self.min_index_pos = 0
        pass
    pass

def create_letter_map(S):
    letter_map = {}
    for idx, char in enumerate(S):
        index_entry = letter_map.get(char, IndexEntry())
        index_entry.index_list.append(idx)
        letter_map[char] = index_entry
    return letter_map
    pass

def move_left(string_to_modify, curr_index, final_pos):
    tail = string_to_modify[curr_index + 1:] if curr_index < (len(string_to_modify) - 1) else ""
    result = string_to_modify[0:final_pos] + string_to_modify[curr_index] + string_to_modify[final_pos:curr_index] + tail
    return result
    pass


def remove_below_min(index_entry: IndexEntry, min_index: int):
    # the list of indices is created in such a way that it should always be sorted
    # so we can use that to ensure the search is fast in the case of big lists
    trim_idx = bisect_left(index_entry.index_list, min_index, lo=index_entry.min_index_pos)  # O(logN)
    index_entry.min_index_pos = trim_idx
    pass

def increment_lower_indices(index_entry: IndexEntry, best_curr_idx: int):
    index_list = index_entry.index_list
    idx = index_entry.min_index_pos
    while index_list[idx] < best_curr_idx:
        index_list[idx] += 1
    pass

def ensure_letter_map_postconditions(letter_map, min_index, just_moved_index):
    # post-condition: list gets to zero, remove from map, and all >= min_index
    chars_to_remove = []
    for char in letter_map:
        remove_below_min(letter_map[char], min_index)  # O(logN)
        if letter_map[char].min_index_pos >= len(letter_map[char].index_list):
            chars_to_remove.append(char)
        else:
            increment_lower_indices(letter_map[char], just_moved_index)
    for char in chars_to_remove:
        letter_map.pop(char)
    pass

def get_first_index(index_entry: IndexEntry):
    return index_entry.index_list[index_entry.min_index_pos]
    pass

def find_best_next(letter_map, min_index, curr_k):
    best_curr_idx = MAX_N
    best_next_idx = MAX_N
    for char in string.ascii_lowercase:  # in alphabetical order
        index_entry = letter_map.get(char, None)
        if index_entry:
            curr_index = get_first_index(index_entry)  # post-condition: list gets to zero, remove from map, and all >= min_index
            next_index = max(min_index, curr_index - curr_k)
            if (next_index < best_next_idx) or (next_index == min_index):
                best_curr_idx = curr_index
                best_next_idx = next_index
            if best_next_idx == min_index:
                break  # you can't do any better on this round
    return best_curr_idx, best_next_idx
    pass

def map_letters_small_k(S, K):
    letter_map = create_letter_map(S)  # O(N)
    curr_k = K
    curr_S = S
    min_index = 0
    while (curr_k > 0) and (len(letter_map) > 0):
        best_curr_idx, best_next_idx = find_best_next(letter_map, min_index, curr_k)
        dist_to_move = best_curr_idx - best_next_idx
        curr_k -= dist_to_move
        best_char = curr_S[best_curr_idx]
        letter_map[best_char].min_index_pos += 1  # remove the first index
        if dist_to_move > 0:  # don't bother moving the char as it's already sorted
            curr_S = move_left(curr_S, best_curr_idx, best_next_idx)
        ensure_letter_map_postconditions(letter_map, best_next_idx, best_curr_idx)
        min_index = best_next_idx + 1
    return curr_S
    pass

def filter_char(S, char_to_filter):
    return [x for x in S if x != char_to_filter]
    pass

def map_letters_large_k(S, N, K):
    curr_k = K
    output_S = ''
    tail_S = list(S)
    for char in string.ascii_lowercase:  # in alphabetical order
        # the index_list is an ordered list of all the positions in which the
        # current character we're examining occur. We keep track of how many
        # previous instances of this letter we've moved (moved_so_far) and
        # then we can use the (index - moved_so_far) to know how far the character
        # will need to move. The most expensive part should be generating the
        # index_list (and perhaps removing the character from the tail, but this
        # can be moved to happen once per character). Index list generation iterates
        # over all the remaining characters in O(N) time to find where each one occurs.
        # However, this only needs to happen a constant number of times (26 letters),
        # so the performance should still be O(N).
        index_list = [idx for idx, char_in_S in enumerate(tail_S) if char_in_S == char]
        moved_so_far = 0
        for idx in range(len(index_list)):
            output_S += char
            distance = (index_list[idx] - moved_so_far)
            moved_so_far += 1
            curr_k -= distance
            tail_S[index_list[idx]] = NULL_CHAR  # mark for later deletion so it's only done once per letter
            if curr_k < N:
                break
        tail_S = filter_char(tail_S, NULL_CHAR)
        if curr_k < N:
            break
    # If we get this far and curr_k >= N it means we have fully sorted the string
    # because otherwise we would have kept going in the above loop. Since there is
    # no more to do we can set curr_k = 0
    if curr_k >= N:
        curr_k = 0
    return output_S + ''.join(tail_S), curr_k
    pass

def map_letters(S, K):
    N = len(S)
    output_S, curr_k = map_letters_large_k(S, N, K) if K >= N else (S, K)
    return map_letters_small_k(output_S, curr_k)  # mop up the rest with the K < N algorithm
    pass

def partialSort(S, K):
    return map_letters(S, K)

# (S = "decade", K = 4) = "adcede"
print(partialSort(S = "decade", K = 4))
# (S = "bbbabbb", K = 2) = "babbbbb"
print(partialSort(S = "bbbabbb", K = 2))
# (S = "abracadabra", K = 15) = "aaaaabrcdbr"
print(partialSort(S = "abracadabra", K = 15))
