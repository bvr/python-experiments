
import sys
import ctypes

def get_clipboard():
    CF_TEXT = 1
    ctypes.windll.user32.OpenClipboard(0)
    try:
        if ctypes.windll.user32.IsClipboardFormatAvailable(CF_TEXT):
            data = ctypes.windll.user32.GetClipboardData(CF_TEXT)
            data_locked = ctypes.windll.kernel32.GlobalLock(data)
            text = ctypes.c_char_p(data_locked)
            value = text.value
            ctypes.windll.kernel32.GlobalUnlock(data_locked)
            return value
    finally:
        ctypes.windll.user32.CloseClipboard()

def set_clipboard(text):
    CF_TEXT = 1
    GMEM_DDESHARE = 0x2000
    ctypes.windll.user32.OpenClipboard(0)
    ctypes.windll.user32.EmptyClipboard()
    try:
        # works on Python 2 (bytes() only takes one argument)
        hCd = ctypes.windll.kernel32.GlobalAlloc(GMEM_DDESHARE, len(bytes(text))+1)
    except TypeError:
        # works on Python 3 (bytes() requires an encoding)
        hCd = ctypes.windll.kernel32.GlobalAlloc(GMEM_DDESHARE, len(bytes(text, 'ascii'))+1)
    pchData = ctypes.windll.kernel32.GlobalLock(hCd)
    try:
        # works on Python 2 (bytes() only takes one argument)
        ctypes.cdll.msvcrt.strcpy(ctypes.c_char_p(pchData), bytes(text))
    except TypeError:
        # works on Python 3 (bytes() requires an encoding)
        ctypes.cdll.msvcrt.strcpy(ctypes.c_char_p(pchData), bytes(text, 'ascii'))
    ctypes.windll.kernel32.GlobalUnlock(hCd)
    ctypes.windll.user32.SetClipboardData(CF_TEXT, hCd)
    ctypes.windll.user32.CloseClipboard()

text = ' '.join(sys.argv[1:])
if len(text) > 0:
    set_clipboard(text)
print(get_clipboard())
