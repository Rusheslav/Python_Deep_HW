import logging
import argparse
from os import stat, walk, path
from collections import namedtuple

CatObject = namedtuple('CatObject', field_names=['Имя_каталога', 'флаг_каталога', 'родительский_каталог'])
FileObject = namedtuple('FileObject', field_names=['Имя_файла', 'Расширениe_файла', 'родительский_каталог'])
FORMAT = '{levelname:<8} - {asctime}: {msg}'
logging.basicConfig(level=logging.INFO, filename='log.log', filemode='a', encoding='utf-8', format=FORMAT, style='{')
logger = logging.getLogger(__name__)

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--path', default=None)
args = parser.parse_args()
addr = args.path

if not addr:
    print('Вы не ввели путь к папке')
if not path.isdir(addr):
    print('По указанному адресу нет каталога')
else:
    logger.info(f'НАЧАЛО ОПИСАНИЯ СОДЕРЖИМОГО КАТАЛОГА ПО АДРЕСУ {path.abspath(addr)}')
    tree = list(walk(addr))
    tree.reverse()

    for obj in tree:
        address, folders, files = obj
        *_, parent, name = address.split('/')
        flag = stat(address).st_flags
        cat_object = CatObject(name, flag, parent)
        logger.info(cat_object)
        for file in files:
            file_name, file_ext = file.split('.')
            file_object = FileObject(file_name, file_ext, parent)
            logger.info(file_object)
