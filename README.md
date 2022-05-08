## Установка
Клонируем репозиторий (возможно необходимо будет связать профиль на GitHub с PyCharm):
![Git_URL](pic/Git_URL.png)
![Get_VCS](pic/Get_VCS.png)

После загрузки устанавливаем интерпретатор:  
![No_interpreter](pic/No_interpreter.png)
![Ok](pic/Ok.png)

Далее нужно активировать среду с помощью команды ```.\venv\Scripts\activate```:  
![Terminal](pic/Terminal.png)
![venv](pic/venv.png)

Вводим по очереди в терминале для установки:
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
Фото и аннотации необходимо сохранить в папке ```Data``` в следующем виде:   
![Data](pic/Data.png)
### 2:
Проверить что в ```object_names_array``` указанны все необходимые объекты:   
![object_names_array](pic/object_names_array.png)
### 3:
Запустить ```main.py```