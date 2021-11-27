import time
# overline_all_text() - Encloses string in unicode overlines regardless of characters.
# Delay - Delay between each key input.
def overline_all_text(delay = 0.12):
    retCode, usr_input = dialog.input_dialog(title='overline_all()', message='Text to overline.')
    if retCode:
        return
    else:
        for c in usr_input:
            keyboard.send_keys(c+'<ctrl>+<shift>+u+0305+')
            time.sleep(delay)
        return

overline_all_text()