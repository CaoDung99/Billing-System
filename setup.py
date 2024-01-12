import cx_Freeze

includefile = ['on2.ico']
excludes = []
packages = []
base = None
if sys.platform == "win32":
    base = "Win32GUI"

shortcut_table = [
    ("DesktopShortcut",
     "DesktopFolder",
     "Billing System",
     "TARGETDIR",
     "[TARGETDIR\\main.exe]",
     None,
     None,
     None,
     None,
     None,
     None,
     "TARGETDIR")
]

msi_data = {'Shortcut': shortcut_table}
bdist_msi_options = {'data': msi_data}

executables = [
    Executable(
        "controller.py",
        base=base,
        icon='on2.ico'
    ),
    Executable(
        "model.py",
        base=base,
        icon='on2.ico'
    ),
    Executable(
        "view.py",
        base=base,
        icon='on2.ico'
    )
]

setup(
    name='YourAppName',
    version='1.0',
    description='Description of your app',
    options={'build_exe': {'include_files': includefile}, 'bdist_msi': bdist_msi_options},
    executables=executables
)