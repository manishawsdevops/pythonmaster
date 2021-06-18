# Translater Exercise.

# Translate the file into Japanese.

from translate import Translator

translator = Translator(to_lang='german')

try:
    with open('test.txt', mode='r') as myfile:
        text = myfile.read()
        translation = translator.translate(text)
        with open('test-german.txt', mode='w') as myfile2:
            myfile2.write(translation)
except FileNotFoundError as err:
    print('File doesnot exist')
