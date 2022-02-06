# This is a sample Python script.
import webbrowser, sys

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

arg = sys.argv[0]


def open(url):
    webbrowser.open(url, 0, True) # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    open(arg)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
