def overline_text():
    retCode, usr_input = dialog.input_dialog(title='overline()', message='Text to overline.')
    for c in usr_input:
        if c.isspace() == True:
            keyboard.send_keys(c)
        else:
            keyboard.send_keys(c+'<ctrl>+<shift>+u+0305+')
    return

overline_text()