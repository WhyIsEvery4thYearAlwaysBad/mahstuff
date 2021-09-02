def underline_text():
    retCode, usr_input = dialog.input_dialog(title='underline()', message='Text to underline.')
    for c in usr_input:
        if c.isspace() == True:
            keyboard.send_keys(c)
        else:
            keyboard.send_keys(c+'<ctrl>+<shift>+u+0332+')
    return

underline_text()