# ------------------------------------------------------------------
# DESCRIPTION
#    Utiliza la técnica End of File (EoF) para agregar o extraer archivos de una cubierta en formato PNG.
#
# OPTIONS
#    -h [secret] [cover] [output]       Agrega información al final de la cubierta
#    -e [cover] [output]                Extrae la información oculta en la cubierta
#
# EXAMPLES
#    $eof_png.py -h secret cover.png output.png
#    $eof_png.py -e secret_cover.png
# ------------------------------------------------------------------

####################################################################
#                           Program start                          #
####################################################################

#!/usr/bin/env python3
import sys
import os

def hide(secret, container, file_output):
    with open(f'{file_output}.png', 'wb') as output:
        try:
            output.write(open(container, 'rb').read())
            try:
                output.write(open(secret, 'rb').read())
                print(f'Se ha ocultado el contenido de "{secret}" dentro de "{file_output}.png".\n')
            except OSError:
                print(f'"{secret}" no es un fichero válido. Por favor, especifique un fichero válido.\n')
        except OSError:
            print(f'"{container}" no es un fichero válido. Por favor, especifique un fichero válido.\n')
        
def extract(container):
    try:
        os.mkdir('Results')
    except OSError:
        pass
    
    with open('./Results/hidden', 'wb') as output1, open(container, 'rb') as cover:
        hidden = cover.read().split(b'IEND\xaeB`\x82')[1]
        output1.write(bytes(hidden))
        print(f'Se ha extraido el contenido oculto en "{container}" dentro de "./results/hidden".\n')
    
    with open('./Results/cover', 'wb') as output2, open(container, 'rb') as cover:
        cover1 = cover.read().split(b'IEND\xaeB`\x82')[0]
        output2.write(bytes(cover1))
        print(f'Se ha extraido la cubierta de "{container}" dentro de "./results/cover".\n')

def parser():
    if len(sys.argv)<3:
        return 'help'
    elif len(sys.argv)<4:
        if (sys.argv[1] == '-e') and (sys.argv[2]):
            return 'extract'
        else:
            return 'help'
    elif len(sys.argv)<6:
        if (sys.argv[1] == '-h') and (sys.argv[2]) and (sys.argv[3]) and (sys.argv[4]):
            return 'hide'
    else:
        return 'help'

def help():
    ayuda = '''
    OPTIONS
    -h [secret] [cover] [output]       Agrega información al final de la cubierta
    -e [cover]                         Extrae la información oculta en la cubierta
    '''
    print(ayuda.strip('\n'))

def banner():
    banner = '''
    =========================================================
        EoF PNG script por Gonzalo Benito
        Email: gu4n4rt@gmail.com
        Github: https://github.com/Guanart
    =========================================================
    '''
    print(banner)

def main():
    banner()
    if parser() == 'extract':
        extract(sys.argv[2])
    elif parser() == 'hide':
        hide(sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        help()

if __name__ == '__main__':
    main()