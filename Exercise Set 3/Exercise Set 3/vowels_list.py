def find_vowels(input_string):
    vowels = 'aeiouAEIOU'
    vowel_list = [char for char in input_string if char in vowels]
    print("Vowels in the string:", vowel_list)

user_input = input("Enter a string: ")
find_vowels(user_input)
