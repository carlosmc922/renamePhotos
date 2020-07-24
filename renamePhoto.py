import os.path
import shutil
import datetime
import os
from PIL import Image

def count_files_in_path(path):
    list = os.listdir(path)
    number_files = len(list)
    print ('*** La carpeta', path, 'contiene', number_files, 'foto/s ***')
    return number_files

def get_date_exif(path):
    return Image.open(path)._getexif()[36867]

def rename_photo(src_dir, dst_dir):
    for filename in os.listdir(src_dir):
        if filename.endswith('.jpg'):
            print('Imagen a renombrar:', filename)
            exif_date = get_date_exif(src_dir+'/'+filename)
            renamed_photo = datetime.datetime.strptime(exif_date, '%Y:%m:%d %H:%M:%S').strftime('%Y%m%d_%H%M%S') + '.jpg'
            print('Imagen renombrada:', renamed_photo)
            shutil.copy(src_dir+'/'+filename, dst_dir+'/'+renamed_photo)
            os.remove(src_dir+'/'+filename)

# Main


count_files_in_path('src')
rename_photo('src', 'dst')
count_files_in_path('dst')