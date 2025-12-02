from pynput import mouse, keyboard
import os
import platform

range_flag = False
x1, y1, x2, y2 = 0, 0, 0, 0

def esc_monitor(key):
    if key == keyboard.Key.esc:
        return False

def click_point(x, y, button, press):
    if button == mouse.Button.left and press == True:
        print('x:{:d} y:{:d}'.format(x, y))

def click_range(x, y, button, press):
    if button == mouse.Button.left and press == True:
        global x1, y1
        x1, y1 = x, y
    elif button == mouse.Button.left and press == False:
        global x2, y2, range_flag
        x2, y2 = x, y
        range_flag = True

def terminal_clear():
    system_name = platform.system()
    if system_name == 'Windows':
        os.system('cls')
    elif system_name == 'Linux' or system_name == 'macOS':
        os.system('clear')

def show_info():
    print('按[1]进入点坐标获取模式')
    print('按[2]进入范围坐标获取模式')
    print('按[3]结束任务')

def position_getpoint():
    print('点击鼠标左键来获取位置, 按下esc退出该模式')
    m_listener = mouse.Listener(on_click = click_point)
    k_listener = keyboard.Listener(on_press = esc_monitor)
    m_listener.start()
    k_listener.start()
    while True:
        if not k_listener.is_alive():
            m_listener.stop()
            terminal_clear()
            break

def position_getrange():
    global range_flag
    print('按下鼠标左键确定开始位置, 释放鼠标左键确定结束位置, 按下esc退出该模式')
    m_listener = mouse.Listener(on_click = click_range)
    k_listener = keyboard.Listener(on_press = esc_monitor)
    m_listener.start()
    k_listener.start()
    while True:
        if not k_listener.is_alive():
            m_listener.stop()
            terminal_clear()
            break
        else:
            if range_flag:
                area = abs(x1 - x2) * abs(y1 - y2)
                print('x_start:{:d} y_start:{:d}'.format(x1, y1))
                print('x_end:{:d} y_end:{:d}'.format(x2, y2))
                print('area:{:d}'.format(area))
                print('')
                range_flag = False

def main():
    while True:
        show_info()
        mode = eval(input())
        match mode:
            case 1:
                position_getpoint()
            case 2:
                position_getrange()
            case 3:
                print('结束任务')
                break
            case _:
                print('无效模式')

if __name__ == '__main__':
    main()
