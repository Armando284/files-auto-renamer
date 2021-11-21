import os
import time
import re
import env

list_name = os.listdir()
list_length = len(list_name)
new_list = []
new_list_updated = []

dot = re.compile(r'\.')
ignoredFileTypes = re.compile(r'.*\.(py|exe|bat|env|git|gitignore|md)\Z')
weirdCharacters = re.compile(r'[^A-Za-z0-9\.]')
numbers = re.compile(r'\d+')
letterAndSpace = re.compile(r'\D+')
defaultText = '\033[3;m'
greenText = '\033[3;32m'
yellowText = '\033[3;33m'
cianText = '\033[3;36m'
redText = '\033[3;31m'


def colorText(color, text):
    colors = env.colors
    if not colors:
        return text
    elif color == 'title':
        return '\033[1;33;45m'+text+defaultText
    elif color == 'green':
        return greenText+text+defaultText
    elif color == 'yellow':
        return yellowText+text+defaultText
    elif color == 'red':
        return redText+text+defaultText
    elif color == 'cian':
        return cianText+text+defaultText
    else:
        return defaultText+text+defaultText


def start():
    print(colorText('title', '  Formateador Automatico de Nombres de Archivos  '))
    time.sleep(1)
    createList()


def createList():
    global list_length, list_name, new_list
    for _file in list_name:
        if not ignoredFileTypes.search(_file) and dot.search(_file):
            new_list.append(_file)
    newListLength = len(new_list)
    _archivo = (' archivo', ' archivos')[newListLength > 0]
    print(colorText('green', '... Cargando '+str(newListLength)+_archivo))
    if newListLength < 1:
        print(colorText('red', 'No hay archivos para renombrar!'))
        end()
        return
    autoRename()
    time.sleep(1)


def autoRename():
    newNameList = []
    clearWord = input(colorText('green', 'Palabra que quieras eliminar: '))
    for _file in new_list:
        nameAndExt = dot.split(_file)
        if len(nameAndExt) < 2:
            print(nameAndExt)
            new_list.remove(_file)
        elif len(nameAndExt) > 2:
            newNameAndExt = ['', '']
            for i in range(len(nameAndExt)-1):
                spacer = (' ', '')[i == 0]
                newNameAndExt[0] = newNameAndExt[0]+spacer+nameAndExt[i]
            newNameAndExt[1] = nameAndExt[len(nameAndExt)-1]
            nameAndExt = newNameAndExt
        cleanName = weirdCharacters.sub(' ', nameAndExt[0])
        startName = startNum(cleanName)
        endName = textName(cleanName, clearWord)
        newName = startName+' - '+endName+'.'+nameAndExt[1]
        newNameList.append(newName)
        print(colorText('cian', 'Nombre original: '+_file))
        print(colorText('yellow', 'Nombre nuevo: '+newName))
    accept(newNameList, new_list)


def startNum(cleanName):
    if numbers.search(cleanName):
        startName = numbers.findall(cleanName)
        if len(startName) > 1:
            print(colorText('cian', 'Posibles numeros en el titulo: '), startName)
            newStartName = input(
                colorText('green', 'Elija el numero correcto: '))
            startName = newStartName
        else:
            startName = startName[0]
    else:
        print(colorText('red', 'No hay ningun numero en el nombre del archivo: '+cleanName))
        startName = input(
            colorText('green', 'Introdusca el numero de este archivo: '))
    startName = int(startName)
    if startName < 10:
        startName = '00'+str(startName)
    elif startName < 100:
        startName = '0'+str(startName)
    else:
        startName = str(startName)
    return startName


def textName(cleanName, clearWord):
    endName = letterAndSpace.findall(cleanName)
    if len(endName) > 1:
        newEndName = ''
        for word in endName:
            newEndName = newEndName+word
        endName = newEndName
    else:
        endName = endName[0]
    if clearWord != '' and re.search(r''+clearWord+'+', endName):
        nameWordsList = re.split(r''+clearWord+'+', endName)
        endName = ''
        for word in nameWordsList:
            endName = endName+word.strip()+' '
    endName = endName.strip()
    endName = endName.title()
    return endName


def accept(newNameList, new_list):
    _accept = input(colorText('green', 'Entra \'ok\' para aceptar: '))
    if _accept != 'ok':
        end(False)
        return
    rename(newNameList, new_list)
    end()


def rename(newNamesList, new_list):
    print(colorText('cian', str(len(newNamesList))+'/'+str(len(new_list))))
    for i in range(len(new_list)):
        os.rename(new_list[i], newNamesList[i])


def end(ok=True):
    time.sleep(1)
    if not ok:
        print(colorText('red', 'Programa detenido por el usuario!'))
        return
    print(colorText('green', '... El programa finalizo con exito!'))


start()
