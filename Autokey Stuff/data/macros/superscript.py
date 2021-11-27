import time
import array
# superscript_text() - Converts characters to super script
# Delay - Delay between each key input.
def superscript_text(delay = 0.12):
    retCode, usr_input = dialog.input_dialog(title='superscript()', message='Text to superscript.')
    if retCode:
        return
    else:
        for c in usr_input:
            superscript_dict={
                '0':'<ctrl>+<shift>+u+2070+',
                '1':'<ctrl>+<shift>+u+00b9+',
                '2':'<ctrl>+<shift>+u+00b2+',
                '3':'<ctrl>+<shift>+u+00b3+',
                '4':'<ctrl>+<shift>+u+2074+',
                '5':'<ctrl>+<shift>+u+2075+',
                '6':'<ctrl>+<shift>+u+2076+',
                '7':'<ctrl>+<shift>+u+2077+',
                '8':'<ctrl>+<shift>+u+2078+',
                '9':'<ctrl>+<shift>+u+2079+',
                '+':'<ctrl>+<shift>+u+207a+',
                '-':'<ctrl>+<shift>+u+207b+',
                '=':'<ctrl>+<shift>+u+207c+',
                '(':'<ctrl>+<shift>+u+207d+',
                ')':'<ctrl>+<shift>+u+207e+',
                'n':'<ctrl>+<shift>+u+207f+'
                }
            keyboard.send_keys(superscript_dict.get(c,""))
            time.sleep(delay)
        return

superscript_text()