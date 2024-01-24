import os
from shutil import copy

from rich.console import Console
from rich.themes import Theme

"""
class organize

"""
custom_theme = Theme({
    'success':'green',
    'error':'bold red',
    'folder':'yellow',
    'file':'#aaffaa',
    'pdf':'#ff0000',
    'docs':'#0000ff',
    'png':'#cb69b8',
    'jpg':'#8087cb',
    'gif':'#8087cb',
    'mp3':'#b8cbac',
    'avi':'#6c681b',
    'mp4':'#4e2e2c',
    'csv':'#13bb74',
    "xlsx":'#21ff00',
    'pptx':'#bb6520',
    'dwg':'#ee8c84',
    'svg':'#906203',
    'psd':'#0c0846',
    'py':'#377790',
    'js':'#e19802',
    'cpp':'#122d46',
    'html':'#cb5f3e',
    'css':'#16c7cb',
    'pages':'#f8ab29',
    'other':'#cb9b83'
})
console = Console(theme=custom_theme)
class Organize:
    """
    Organizes files from a source directory to a destination directory

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
    
    
    def organizeElement(self,rootPath:str, destPath='' , delete:bool = False) -> None:
        """
        organize elements from src directory to destination directory

        Args:
            rootPath (str): [source directory]
            destPath (str): [destination directory]
            delete (bool): [delete files from src directory] default = False

        
        
        """
        
        if(destPath == '' or destPath==' '):
            os.mkdir(rootPath+'organize')
            destPath = rootPath+'organize/'

        
        folderlist = []
        for file in os.listdir(rootPath):
            name,ext = os.path.splitext(rootPath + file)  
            # discarting folders
            if ext in ['']:
                if '.' in name:
                    print(name)
                else:
                    folderlist.append(name)

            else:
                tp = ext.split('.')
                name = name.split('/')
                name = name[-1]
                # if it doesn't exist, create folder
                if(os.path.exists(destPath+tp[1])==False):
                    os.mkdir(destPath+tp[1])
                text = '[{}] {} [/{}]'.format(tp[1],name+ext,tp[1])
                console.print(text)
                copy(rootPath + file, destPath+tp[1]+'/' + name[:-1] + ext)
                # print(rootPath+name+ext)
                if(delete == True):
                    os.remove(rootPath+name+ext)

        for i in range(len(folderlist)):
            aux = folderlist[i].split('/')
            aux = aux[-1]
            if (os.path.exists(destPath+aux) != True):
                os.mkdir(destPath+aux)
                self.organizeElement(folderlist[i]+'/',destPath+aux+'/')
