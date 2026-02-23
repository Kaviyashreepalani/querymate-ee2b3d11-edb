from collections import defaultdict

def find_anagrams(words):
    """
    Finds groups of anagrams from a list of words.

    Args:
        words: A list of strings.

    Returns:
        A list of lists, where each inner list contains words that are anagrams of each other.
    """
    anagram_groups = defaultdict(list)

    for word in words:
        # Normalize the word by sorting its characters
        # This creates a unique key for each set of anagrams
        normalized_word = "".join(sorted(word.lower()))
        anagram_groups[normalized_word].append(word)

    # Filter out groups with only one word, as they are not anagrams of anything else
    return [group for group in anagram_groups.values() if len(group) > 1]

# Example Usage:
word_list1 = ["listen", "silent", "enlist", "hello", "world", "act", "cat", "tac", "elbow", "below", "bellow"]
anagrams1 = find_anagrams(word_list1)
print(f"Anagrams in word_list1: {anagrams1}")

word_list2 = ["apple", "banana", "aple", "plea"]
anagrams2 = find_anagrams(word_list2)
print(f"Anagrams in word_list2: {anagrams2}")

word_list3 = ["a", "b", "c"]
anagrams3 = find_anagrams(word_list3)
print(f"Anagrams in word_list3: {anagrams3}")