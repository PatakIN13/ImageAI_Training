import os
import shutil
from xml.etree import ElementTree as et
from imageai.Detection.Custom import DetectionModelTrainer



class Folders:
    folder_train: str = 'example/train'
    folder_validation: str = 'example/validation'
    folder_image: str = 'images'
    folder_annotations: str = 'annotations'


def find_files(folder, types):
    """
    Функция поиска нужных файлов
    :param folder: Папка с файлами
    :param types: Тип файлов
    :return: Массив имен файлов
    """
    return [entry.name for entry in os.scandir(folder) if
            (entry.is_file() and os.path.splitext(entry.name)[1].lower() in types)]


def create_folders():
    """
    Функция создания папок
    """

    os.makedirs(Folders.folder_train, exist_ok=True)
    os.makedirs(Folders.folder_validation, exist_ok=True)
    os.makedirs(Folders.folder_train + '/' + Folders.folder_image, exist_ok=True)
    os.makedirs(Folders.folder_train + '/' + Folders.folder_annotations, exist_ok=True)
    os.makedirs(Folders.folder_validation + '/' + Folders.folder_image, exist_ok=True)
    os.makedirs(Folders.folder_validation + '/' + Folders.folder_annotations, exist_ok=True)


def copy_files(photo_name):
    """
    Функция копирования файлов

    :param photo_name:  Имя фото
    """
    create_folders()
    count = 5
    name = photo_name[:-4]
    types = photo_name[-4:]
    tree = et.parse("Data/{}.xml".format(name))

    for i in range(count):
        end_photo = name + str(i) + types
        end_folder = "{}/{}/images/".format(os.getcwd(), Folders.folder_train)
        tree.find('.//filename').text = end_photo
        tree.find('.//path').text = end_folder + end_photo
        tree.write(Folders.folder_train + "/annotations/{}{}.xml".format(name, str(i)))
        shutil.copy2(r'Data/{}'.format(photo_name), r'{}/images/{}'.format(Folders.folder_train, end_photo))

    for i in range(count, count + int(count * 0.2)):
        end_photo = name + str(i) + types
        end_folder = "{}/{}/images/".format(os.getcwd(), Folders.folder_validation)
        tree.find('.//filename').text = end_photo
        tree.find('.//path').text = end_folder + end_photo
        tree.write(Folders.folder_validation + "/annotations/{}{}.xml".format(name, str(i)))
        shutil.copy2(r'Data/{}'.format(photo_name), r'{}/images/{}'.format(Folders.folder_validation, end_photo))


photos = find_files("Data", [".JPG", ".jpg"])
for el in photos:
    copy_files(el)

trainer = DetectionModelTrainer()
trainer.setModelTypeAsYOLOv3()
trainer.setDataDirectory(data_directory="example")

trainer.setTrainConfig(object_names_array=["gap", "spike"], batch_size=4, num_experiments=200, train_from_pretrained_model="pretrained-yolov3.h5")


trainer.trainModel()
