# Guess the word with 4 hints to help
# Rationale: Practice word slicing
# Type of exercise: Finish the code
original_word = "recommendation"
scrambled_word = "eoommandretnic"
# Create the hint slices...
hint1_slice = original_word[4:6] # TO DO Create the word slice according to the clue below, use the format "original_word[x:y]"
hint2_slice = original_word[-3:] # TO DO Create the word slice according to the clue below, use the format "original_word[x:y]"
hint3_slice = original_word[7:10] # TO DO Create the word slice according to the clue below, use the format "original_word[x:y]"
hint4_slice = original_word[:2] # TO DO Create the word slice according to the clue below, use the format "original_word[x:y]"

# Game instructions
print("Scrambled word:", scrambled_word)
print("Guess the original word from the scrambled version.")
print("Here are some hints:")

# Hints based on list slicing
print("Hint 1: The 5th and 6th letters are '" + hint1_slice + "'.")
print("Hint 2: The last 3 letters are '" + hint2_slice + "'.")
print("Hint 3: The 8th to 10th letters are '" + hint3_slice + "'.")
print("Hint 4: The first two letters are '" + hint4_slice + "'.")
# Game ends here
print("What's your guess?")