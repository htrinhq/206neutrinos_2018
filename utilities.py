##
## EPITECH PROJECT, 2018
## 206neutrinos_2018
## File description:
## utilities.py

from sys import stderr

def helper() -> None:
    """Display the prgram usage."""
    print('USAGE',
            '\t./206neutrinos n a h sd\n',
            'DESCRIPTION',
            '\tn\tnumber of values',
            '\ta\tarithmetic mean',
            '\th\tharmonic mean',
            '\tsd\tstandard deviation',
            sep='\n', end='\n')

def error(str: str) -> None:
    """Write error msg on error output then exits 84."""
    str = str + '\n'
    stderr.write(str)
    exit(84)


