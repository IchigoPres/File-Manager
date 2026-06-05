import tkinter as tk

"""
class tkinter.Tk(screenName=None,
                 baseName=None,
                 className='Tk',
                 useTk=True,
                 sync=False,
                 use=None)
"""

def default_function(): print("Clicked")
def vector2(x, y): return {"x": x, "y": y}
class WindowTKinter:
    def __init__(self, width, height, title):
        self.root = tk.Tk()
        self.root.title(title)
        self.root.geometry(str(width) + "x" + str(height))
    def addButton(self,
                  text,
                  function=default_function,
                  foreground="#000000",
                  background="#ffffff",
                  position=vector2(0, 0),
                  font=("Arial", 12)):
        button = tk.Button(
            self.root,         # class <tk.Tk>
            text=text,         # str
            command=function,  # def function()
            fg=foreground,     # str ex. "#ffffff" or "white"
            bg=background,     # str ex. "#000000" or "black"
            font=font          # ex. font=("Arial", 12)
        )
        button.pack(padx=position["x"], pady=position["y"])
        return button
    def addLabel(self, text, position=vector2(0, 0), font=None):
        label = tk.Label(
            self.root,    # class <tk.Tk>
            text=text,    # str
            font=font     # ex. font=("Arial", 12)
        )
        label.pack(padx=position["x"], pady=position["y"])
        return label
    def addEntry(self, placeholder, width, height, position=vector2(0, 0), font=None):
        entry = tk.Entry(
            root,          # class <tk.Tk>
            width=width,   # int
            height=height, # int
            font=font      # ex. font=("Arial", 12)
        )
        entry.insert(0, placeholder)
        entry.pack(padx=position["x"], pady=postion["y"])
        return entry
    def start(self):
        self.root.mainloop()

class File:
    def __init__(self, filepath):
        self.filepath = filepath
    def isDir(self): return os.path.isdir(self.filepath)
    def getFiles(self):
        if not self.isDir(): return None
        return os.listdir(self.filepath)
    def cdIndex(self, file_index):
        files = self.getFiles()
        if not files: return None
        self.filepath = self.filepath + "/" + files[file_index]
    def read(self, index):
        files = self.getFiles()
        if not files: return None
        toRead = self.filepath + "/" + files[index]
        with open(toRead, "r") as file:
            return file.read()
    def readBytes(self, index):
        files = self.getFiles()
        if not files: return None
        toRead = self.filepath + "/" + files[index]
        with open(toRead, "rb") as file:
            return file.read()
    def write(self, index, content):
        files = self.getFiles()
        if not files: return None
        toWrite = self.filepath + "/" + files[index]
        with open(toWrite, "w") as file:
            return file.write(content)
    def writeBytes(self, index, content):
        files = self.getFiles()
        if not files: return None
        toWrite = self.filepath + "/" + files[index]
        with open(toWrite, "wb") as file:
            return file.write(content)
