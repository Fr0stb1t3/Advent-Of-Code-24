from library import timer
with open("input/input19.txt") as f:
# with open("sample/sample19.txt") as f:
    available_patterns,designs = f.read().strip().split("\n\n")
    available_patterns = available_patterns.split(", ")
    designs=designs.splitlines()

# print(available_patterns)
# print("*"*100)
# print(designs)

def is_word_constructable(char_list, target_word):
    def can_construct(word, chars):
        # Base case: if word is empty, construction is successful
        if not word:
            return True
        
        # Try matching each character/multi-character element
        for char in chars:
            if word.startswith(char):
                # Recursively check remaining word (characters can be reused)
                if can_construct(word[len(char):], chars):
                    return True
        
        return False

    return can_construct(target_word, char_list)

def count_combinations_dp(char_list, target_word):
    # Initialize DP table
    dp = [0] * (len(target_word) + 1)
    dp[0] = 1  # Base case: empty string
    
    # Iterate through each character position
    for i in range(1, len(target_word) + 1):
        # Try each character from the list
        for char in char_list:
            # Check if character matches word ending
            if i >= len(char) and target_word[i-len(char):i] == char:
                dp[i] += dp[i - len(char)]
    # print(f"{target_word}: {dp}")
    return dp[len(target_word)]
@timer
def part1():
    sol=0
    for word in designs:
        result=is_word_constructable(available_patterns, word)
        if result:
            sol+=1
        # print(f"{word}: {is_word_constructable(available_patterns, word)}")
    return sol
@timer
def part2():
    valid_words=[]
    for word in designs:
        result=is_word_constructable(available_patterns, word)
        if result:
            valid_words.append(word)
    sol=0
    for word in valid_words:
        # print(f"{word}: {count_combinations_dp(available_patterns, word)}")
        combinations=count_combinations_dp(available_patterns, word)
        sol+=combinations
    return sol
print("Part 1:",part1())
print("Part 2:",part2())
