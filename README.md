## Установка
Для запуска нужно установить через: ``` pip install -r requirements.txt```  

Или в ручную:
```
pip install tensorflow
pip install opencv-python
pip install keras
pip install imageai
```
### Скачать предварительную модель [yolov3](https://github.com/OlafenwaMoses/ImageAI/releases/download/essential-v4/pretrained-yolov3.h5)
Сохранить ее в корне проекта


## Работа
### 1:
Фото и анотации необходимо сохранить в папке ```Data``` в следующем виде:   
![Data](pic/Data.png)
### 2:
Проверить что в ```object_names_array``` указанны все необходимые объекты:   
![object_names_array](pic/object_names_array.png)
### 3:
Запустить ```main.py```