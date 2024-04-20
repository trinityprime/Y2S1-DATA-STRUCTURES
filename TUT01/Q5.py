def vowel_generator(sentence):
    vowels = ["a", "e", "i", "o", "u"]
    counter = 0
    for i in sentence:
        if i.lower() in vowels:
            counter += 1
            print(i)

    return f"{counter} vowels detected"


print(vowel_generator("hahahaha"))
