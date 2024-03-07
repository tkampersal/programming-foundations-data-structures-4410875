def has_unique_characters(data):
    letter_set = set([ltr for ltr in data]) 
    letter_set2 = set(data)
    print(letter_set)
    print(letter_set2)
    if len(data) == len(letter_set):
        print(f"'{data}' has unique characters!!!")
    else:
        print("'" + data + "'" + "DOES NOT have unique characters!!!")


print(has_unique_characters('sample'))
print(has_unique_characters('hello world'))
print(has_unique_characters('linkedin'))
print(has_unique_characters('python'))
