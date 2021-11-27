import time
import array
# subscript_text() - Converts characters to super script
# Delay - Delay between each key input.
def subscript_text(delay = 0.12):
    retCode, usr_input = dialog.input_dialog(title='subscript()', message='Text to subscript.')
    if retCode:
        return
    else:
        for c in usr_input:
            subscript_dict={
                '0':'<ctrl>+<shift>+u+2080+',
                '1':'<ctrl>+<shift>+u+2081+',
                '2':'<ctrl>+<shift>+u+2082+',
                '3':'<ctrl>+<shift>+u+2083+',
                '4':'<ctrl>+<shift>+u+2084+',
                '5':'<ctrl>+<shift>+u+2085+',
                '6':'<ctrl>+<shift>+u+2086+',
                '7':'<ctrl>+<shift>+u+2087+',
                '8':'<ctrl>+<shift>+u+2088+',
                '9':'<ctrl>+<shift>+u+2089+',
                '+':'<ctrl>+<shift>+u+208a+',
                '-':'<ctrl>+<shift>+u+208b+',
                '=':'<ctrl>+<shift>+u+208c+',
                '(':'<ctrl>+<shift>+u+208d+',
                ')':'<ctrl>+<shift>+u+208e+',
                'n':'<ctrl>+<shift>+u+208f+'
                }
            keyboard.send_keys(subscript_dict.get(c,""))
            time.sleep(delay)
        return

subscript_text()