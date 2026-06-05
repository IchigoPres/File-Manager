import os
import sys
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
