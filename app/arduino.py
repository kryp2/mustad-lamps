import time

def set_no_color(my_board, lamp, my_hexcolor):
    for pin in lamp:
         my_board.pwm_write(pin, 0)

def set_hexcolor(my_board, lamp, my_hexcolor):
    rgb = 0
    print(my_hexcolor)
    if my_hexcolor[0] == '#':
        rgb = rgb + 1
    for pin in lamp:
        split = rgb + 2
        intensity = my_hexcolor[rgb:split] 
        my_board.set_pin_mode_pwm_output(pin)
        my_board.pwm_write(pin, int(intensity, 16))
        rgb = rgb + 2

def set_blink(my_board, lamp, my_hexcolor):
    while True:
        set_hexcolor(my_board, lamp, my_hexcolor)
        time.sleep(0.5)
        set_no_color(my_board, lamp, my_hexcolor)
        time.sleep(0.5)
