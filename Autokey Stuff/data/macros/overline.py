import time
# overline_text() - Encloses characters in unicode overlines. Ignores spaces.
# Delay - Delay between each key input.
def overline_text(delay = 0.12):
    retCode, usr_input = dialog.input_dialog(title='overline()', message='Text to overline.')
    if retCode:
        return
    else:
        for c in usr_input:
            if c.isspace() == True:
                keyboard.send_keys(c)
                time.sleep(delay)
            else:
                keyboard.send_keys(c)
                time.sleep(delay)
                keyboard.send_keys('<ctrl>+<shift>+u+0305+')
                time.sleep(delay)
        return

overline_text()