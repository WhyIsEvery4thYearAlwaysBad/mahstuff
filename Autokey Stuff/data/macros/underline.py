import time
# underline_text() - Encloses characters in unicode underlines. Ignores spaces.
# Delay - Delay between each key input.
def underline_text(delay = 0.12):
    retCode, usr_input = dialog.input_dialog(title='underline()', message='Text to underline.')
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
                keyboard.send_keys('<ctrl>+<shift>+u+0332+')
                #keyboard.send_keys('̲')
                time.sleep(delay)
        return

underline_text()