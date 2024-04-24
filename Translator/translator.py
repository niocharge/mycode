from translate import Translator
translator = Translator(to_lang="ja")
text = input('Write a thing you want to translate: ')

try:
    with open('test.txt', mode='w') as my_file:
        text1 = my_file.write(text)
        translation = translator.translate(text)
        print(translation)
        with open('test-ja.txt', mode='w', encoding="utf-8") as my_file2:
            my_file2.write(translation)
except FileNotFoundError as e:
    print('Check your file path!')
