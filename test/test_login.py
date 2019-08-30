from pywinauto import Desktop, Application, keyboard, findwindows
import time
import pytest
import PyInstaller.__main__
import os

# Globals
app = None
dlg = None

def build_app():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, '../vc_api_main.py')

    name = ("{}{}".format(dirname, "/build")).replace('\\', '/')

    PyInstaller.__main__.run([
        filename,
        '--name=VCenter API',
        '--windowed',
        '--distpath={}'.format(name),
        '--specpath={}'.format(name),
        '--workpath={}/workspace'.format(name),
    ])


def setup_function():
    """ setup any state tied to the execution of the given function.
    Invoked for every test function in the module.
    """
    global app, dlg
    app_file = "{}{}".format(os.path.dirname(__file__), "/build/VCenter API/VCenter API.exe")
    print(os.path.isfile(app_file))
    if not os.path.isfile(app_file):
        build_app()
    time.sleep(1)
    cmd_file = app_file.replace("/", "\\")
    app = Application().start(cmd_line=cmd_file)
    qtqwindowicon = app.Qt5QWindowIcon
    qtqwindowicon.wait('ready')
    dlg = Desktop().VCenter_API


def teardown_function():
    """ teardown any state that was previously setup with a setup_function
    call.
    """
    global app, dlg
    dlg.close()
    app.kill()

def test_bad_hostname():
    global dlg
    dlg.type_keys(u'bad{SPACE}hostname')
    keyboard.send_keys(u'{ENTER}')
    time.sleep(1)
    mywindows = findwindows.find_windows(
        class_name="Qt5QWindowIcon", title="Error")
    time.sleep(1)
    assert len(mywindows) > 0
    if len(mywindows):
        keyboard.send_keys(u'{ENTER}')
