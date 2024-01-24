import click
from click_help_colors import HelpColorsGroup, HelpColorsCommand
from rich.console import Console
from rich.themes import Theme
from functions.organize import Organize
from functions.copyE import CopyElements


custom_theme = Theme({
    'success':'green',
    'error':'bold red'
})
console = Console(theme=custom_theme)


# red , green , yellow , blue , magenta , cyan , white , black


@click.group(
    cls=HelpColorsGroup,
    help_headers_color='magenta',
    help_options_color='cyan',
    help_options_custom_colors={'organize': 'red'}      
)
def main():
    pass

DELETE = {
    'y':True,
    'n':False
}

TYPE = {
    'y':True,
    'n':False
}


# rootPath:str, destPath='' , delete:bool = False, type:bool = False
@main.command(
    
    cls=HelpColorsCommand,
    help_headers_color=None,
    help_options_color=None,  
    help_options_custom_colors={'--src': 'green'}  
)
@click.option('--src','-s',prompt='Source Dir: ', help='src directory')
@click.option('--dest', '-d', prompt='Destination Dir: ', help='dest directory')
@click.option('--remove','-r',prompt='Delete files from src : ', type=click.Choice(DELETE.keys()))
@click.option('--file','-f',prompt='organize by files : ', type=click.Choice(TYPE.keys()))
def organize(src,dest,remove,file):
    
    # console.print(src,dest,delete,tipo)
    
    # '/Users/disp_excript/Desktop/original/'
    # '/Users/disp_excript/Desktop/copia/'
    # '/Users/disp_excript/Desktop/organizado/'
    
    if (TYPE.get(file) == True):
        fold = Organize()
        root = fold.RootPath(src)
        desti = fold.DestPath(dest)
        print('organizado')
        print(TYPE.get(file))
        fold.organizeElement(rootPath=root,destPath=desti,delete=DELETE.get(remove))
    else:
        foldCopy = CopyElements()
        root = foldCopy.RootPath(src)
        desti = foldCopy.DestPath(dest)
        print(TYPE.get(file))
        print('copiado')
        foldCopy.copyElements(rootPath=root, destPath=desti,delete=DELETE.get(remove))





if __name__ == '__main__':
    main()