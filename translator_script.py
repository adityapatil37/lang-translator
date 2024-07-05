from googletrans import Translator

translator = Translator()
text = input("enter text: ")
detected_language = translator.detect(text)
print(f"Detected language: {detected_language.lang}")
translation = translator.translate(text, dest='en')
print(f"Translated text: {translation.text}")