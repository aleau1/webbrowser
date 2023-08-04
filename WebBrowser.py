#!/usr/bin/env python 3.11.2
class StringTypedProperty:
    def __init__(self):
        self.__string__property__ = None

    @property
    def string_property(self):
        return self.__string__property__
    @string_property.setter
    def string_property(self, new):
        if isinstance(new, str):
            self.__string__property__ = new
        else:
            self.__string__property__ = None

class Filename(StringTypedProperty):
    def __init__(self):
        StringTypedProperty.__init__(self)
        self.__filename__ = None
    
    @property
    def filename(self):
        return self.__filename__
    @filename.setter
    def filename(self, new):
        self.string_property = new
        self.__filename__ = self.string_property

from os.path import exists, isdir, realpath
class Folder(StringTypedProperty):
    def __init__(self, folder:str):
        StringTypedProperty.__init__(self)
        self.folder = folder
    
    @property
    def folder(self):
        return self.__folder__
    @folder.setter
    def folder(self, new:str):
        try:
            __realpath__ = realpath(new)
            if exists(__realpath__) and isdir(__realpath__):
                self.string_property = __realpath__
                self.__folder__ = self.string_property
        except:
            self.string_property = None
            self.__folder__ = None

import subprocess

class StandardOutput:
    @staticmethod
    def stdout(system_command:str):
        stdout = subprocess.check_output(system_command, shell=True, text=True, stderr=subprocess.STDOUT)
        return stdout

class WhoAmI(StandardOutput):
    def whoami(self):
        full_string = super().stdout("powershell.exe whoami").rstrip('\n').split('\\')
        hostname, username = full_string[0], full_string[1]
        return hostname, username

class DownloadFolder(Folder):
    def __init__(self):
        Folder.__init__(self, None)
        self.folder = realpath(f"C:\\Users\\{WhoAmI().whoami()[1]}\\Downloads")
        self.__download_folder__ = self.__folder__
    @property
    def download_folder(self):
        return self.__download_folder__

class FileExtensionFilter:
    def fetch_file_extension(self, filename:str) -> str:
        try:
            if filename.__contains__('.'):
                return filename.split('.')[-1]
            return None
        except:
            return None

class FileExtension(StringTypedProperty, FileExtensionFilter):
    def __init__(self):
        StringTypedProperty.__init__(self)
        self.__file_extension__ = None

    @property
    def file_extension(self):
        return self.__file_extension__
    @file_extension.setter
    def file_extension(self, new):
        self.string_property = new
        self.__file_extension__ = self.string_property

class ComplexFilename(FileExtension, Filename):
    def __init__(self, filename:str):
        FileExtension.__init__(self)
        Filename.__init__(self)
        self.file_extension = super().fetch_file_extension(filename)
        self.filename = filename

from os.path import join
class OmegaPath(Folder, ComplexFilename):
    def __init__(self, folder, filename):
        Folder.__init__(self, folder)
        ComplexFilename.__init__(self, filename)
        try:
            fullpath = join(self.folder, self.filename)
            if exists(fullpath):
                self.__fullpath__ = join(self.folder, self.filename)
            else:
                raise FileExistsError(f"{fullpath}")
        except:
            self.__fullpath__ = None

    @property
    def path(self):
        return self.__fullpath__

from keyboard import send
import subprocess, shlex
class WebBrowser(OmegaPath, DownloadFolder):
    def __init__(self, folder:str, web_browser_exec:str):
        OmegaPath.__init__(self, folder, web_browser_exec)
        DownloadFolder.__init__(self)
    def terminate(self):
        send("alt+f4")
    def browse(self, url:str):
        try:
            self._subprocess = subprocess.Popen(
                shlex.split(f"'{self.path}' --new-window '{url}'"))
        except:
            raise AttributeError('This web browser is not installed at specified location. ')



if __name__ == "__main__":
    raise NotImplementedError()