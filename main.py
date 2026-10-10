import keyboard
import pyautogui


with open("input.txt", "r", encoding="utf-8") as file:
    text = file.read()


def type_text():
    pyautogui.write(text)


def cleantext(text):
    text = text.lower()
    text = text.replace(" ", "")
    text = text.replace("\n", " ")
    text = text.replace("  ", " ")

    text = text.replace("ö", "oe")
    text = text.replace("ä", "ae")
    text = text.replace("ü", "ue")
    text = text.replace("-", "")
    text = text.replace(".", "")

    return text


trigger_key = "f2"

text = cleantext(text)
keyboard.add_hotkey(trigger_key, type_text)

print(f"Press '{trigger_key}' to enter the text. Press 'Esc' to exit.")

keyboard.wait("esc")
