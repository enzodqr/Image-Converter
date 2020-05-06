from sys import argv
from os import path, mkdir, listdir
from PIL import Image


directory_path = argv[1:]  # [existing directory, new directory]


def get_path(directory_path):
    ''' return the directory path where the files
        are going to be store: ./existing directory/new directory '''
    return '/'.join(directory_path)


def img_convertion(directory_path):
    img_file = directory_path[0]
    directory = get_path(directory_path)

    for img in listdir(img_file):
        if img.endswith('.jpg'):
            img_name = path.splitext(img)[0]
            new_img = Image.open(f'{img_file}/{img}')
            new_img.save(f'{directory}/{img_name}.png', 'png')


def check_directory(directory_path):
    directory = get_path(directory_path)
    try:
        if not path.exists(directory):
            mkdir(directory)
        img_convertion(directory_path)
    except FileExistsError as error:
        print('File does not exist.')
        raise error
    except FileNotFoundError as error:
        print('File not found.')
        raise error


if __name__ == "__main__":
    check_directory(directory_path)
