from pynput.keyboard import Key, Controller, Listener, GlobalHotKeys, KeyCode

kbc = Controller()

t = 'שלום עולם!'
# for c in t:
#     vk = KeyCode.from_char(c)
#     print(vk)
#     kc = KeyCode.from_vk(vk)
#     kbc.tap(kc)
kbc.tap('a')
kbc.tap('ש')
# kbc.type(t)

# with keyboardController.pressed(Key.shift):
#     keyboardController.tap(Key.alt_l)