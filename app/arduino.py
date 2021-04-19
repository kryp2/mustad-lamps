def set_hexcolor(my_board, lamp, my_hexcolor):
    rgb = 0
    split = rgb + 2
    for pin in lamp:
        intensity = my_hexcolor[rgb:split] 
        my_board.set_pin_mode_pwm_output(pin)
        my_board.pwm_write(pin, int(intensity, 16))
        rgb = rgb + 2
        split = split + 2
        