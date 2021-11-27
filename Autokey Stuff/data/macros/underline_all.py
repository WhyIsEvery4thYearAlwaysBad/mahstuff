import time
# underline_all_text() - Encloses string in unicode underlines regardless of character.
# Delay - Delay between each key input.
def underline_all_text(delay = 0.12):
    retCode, usr_input = dialog.input_dialog(title='underline_all()', message='Text to underline.')
    if retCode:
        return
    else:
        for c in usr_input:
            keyboard.send_keys(c+'<ctrl>+<shift>+u+0332+')
            time.sleep(delay)
        return

underline_all_text()