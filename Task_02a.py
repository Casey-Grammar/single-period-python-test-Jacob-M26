# Task 02a - Count Vowels
# Write a function called count_vowels(text)
# that returns the number of vowels in the string.
# Count both uppercase and lowercase vowels.
#
# Vowels are: a, e, i, o, u
#
# Example:
# count_vowels("Education") -> 5

def count_vowels(text):
    # Write your code here
    vowels = "aeiou"
    count_vowels = 0
    
    # Iterate through each character in the input string
    for char in text.lower():
        # Check if the character is in the vowel string
        if char in vowels:
            count_vowels += 1
            
    return count_vowels


def main():
    text = input("Enter text: ")
    print(count_vowels(text))


if __name__ == "__main__":
    main()
