pyside6-uic main.ui > ui_main.py
sed -i '.bak' 's/import resources_rc/from . resources_rc import */' ui_main.py
mv ui_main.py ./modules/

pyside6-rcc resources.qrc -o resources_rc.py
mv resources_rc.py ./modules/

rm ui_main.py.bak