def count_vow(word):
    count = 0
    for w in word:
        if w in ("a", "e", "i", "o", "u"):
            count += 1
    return count

word = input("Enter a word: ").lower()
# char = list(word)
# print(char)

vow = count_vow(word)

print(f"No. of vowels = {vow} and no of consonants = {len(word)-vow}")

