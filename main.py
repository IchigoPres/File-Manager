import os
import sys
from Window import WindowTKinter
from Window import vector2
from Window import File

base = File(sys.argv[1])
base.cdIndex(int(sys.argv[2], base=10))
print(base.filepath)


#
# def doSomething(): return None
#
# window = WindowTKinter(300, 300, "My Window")
# window.addButton(
#     "doSomething",
#     doSomething,
#     position=vector2(0, 0)
# )
# window.start()
