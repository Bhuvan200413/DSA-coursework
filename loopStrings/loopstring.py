#counting Characters in a string
'''

def count_characters(text):
    count = 0
    for character in text:
        count += 1
    return count
def main():
    text = input("Enter a String: ")
    print("Characters count: ", count_characters(text))
main()'''

#count if a string contains a vowel
'''def count_vowels(text):
    count = 0
    vowels ='aeiouAEIOU'
    for char in text:
        if char in vowels:
            count += 1
    return count 
def main():
    text = input("Enter a string:")
    print("Vowels count: ", count_vowels(text))
main()'''

#reversing a string

def rev_string(text):
    reversed_text =""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text    
Text = input("Enter a string: ")
print("Reversed string: ", rev_string(Text))