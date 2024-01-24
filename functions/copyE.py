import os
from shutil import copy

from rich.console import Console
from rich.themes import Theme

"""
class CopyElements

"""
custom_theme = Theme({
    'success':'green',
    'error':'bold red',
})
console = Console(theme=custom_theme)
class CopyElements:
    """
    Copy files from a source directory to a destination directory

    Attributes:
        src (str): [Source Directory]
        dest (str): [Destination Directory]
    """

    def __init__(self) -> None:
        """
        Initializes Atrributes

        """
        self.src = ''
        self.dest = ''
        

    def RootPath(self,src:str) -> str:
        """
        Save value of src dir

        Args:
            src (str) : [Source Directory]
        """
        self.root = src
        return self.root
    
    def DestPath(self,dest:str) -> str:
        """
        Save value of dest dir

        Args:
            dest (str) : [Destination Directory]
        """
        self.dest = dest
        return self.dest
    
    def copyElements(self,rootPath:str,destPath:str,delete:bool=False) -> None:
        """
        copy elements from src directory to destination directory

        Args:
            rootPath (str): [source directory]
            destPath (str): [destination directory]

        Examples
        --------
        >>> copyElements('/desktop/example1/', '/desktop/example2/')

        
        """
        try:
            folderlist = []
            # print(rootPath)
            for file in os.listdir(rootPath):
                # print(file)
                name,ext = os.path.splitext(rootPath + file)  
                if ext in ['']:
                    if '.' in name:
                        print(name)
                    else:
                        folderlist.append(name)
                else:
                    name = name.split('/')
                    name = name[-1]
                    copy(rootPath + file, destPath + name + ext)
                    os.remove(rootPath+name+ext)

            for i in range(len(folderlist)):
                aux = folderlist[i].split('/')
                aux = aux[-1]
                if (os.path.exists(destPath+aux) != True):
                    os.mkdir(destPath+aux)
                    self.copyElements(folderlist[i]+'/',destPath+aux+'/')
        except:
            console.print('[error]Sorry, an error ocurred [/error]')

    