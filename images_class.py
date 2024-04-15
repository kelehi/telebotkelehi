import os
from random import choice
from PIL import Image, ImageFilter
import string


class Filter:
    def __init__(self, file_name):
        self.file_name = file_name
        self.script_1 = self.__script_filter()

    def __script_filter(self) -> str:
        list_random = ['CONTOUR', 'EDGE_ENHANCE', 'EDGE_ENHANCE_MORE', 'EMBOSS', 'FIND_EDGES', 'SHARPEN',
                       'SMOOTH', 'SMOOTH_MORE']

        list_choice = choice(list_random)
        original = Image.open(self.file_name)
        img = None

        if list_choice == 'CONTOUR':
            img = original.filter(ImageFilter.CONTOUR)

        elif list_choice == 'EDGE_ENHANCE':
            img = original.filter(ImageFilter.EDGE_ENHANCE)

        elif list_choice == 'EDGE_ENHANCE_MORE':
            img = original.filter(ImageFilter.EDGE_ENHANCE_MORE)

        elif list_choice == 'EMBOSS':
            img = original.filter(ImageFilter.EMBOSS)

        elif list_choice == 'FIND_EDGES':
            img = original.filter(ImageFilter.FIND_EDGES)

        elif list_choice == 'SHARPEN':
            img = original.filter(ImageFilter.SHARPEN)

        elif list_choice == 'SMOOTH':
            img = original.filter(ImageFilter.SMOOTH)

        elif list_choice == 'SMOOTH_MORE':
            img = original.filter(ImageFilter.SMOOTH_MORE)

        string_random = ''.join([choice([element for element in string.ascii_letters]) for _ in range(10)])
        file_name = f'stage{string_random}.png'
        img.save(file_name)

        return file_name

    def delete(self):
        os.remove(self.file_name)
        os.remove(self.script_1)

