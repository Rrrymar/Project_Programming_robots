# Используем базовый образ ROS
FROM osrf/ros:noetic-desktop-full

# Устанавливаем зависимости
RUN apt-get update && apt-get install -y python3-pip

# Копируем файлы проекта в контейнер
COPY . /catkin_ws/src/my_robot_project

# Устанавливаем Python зависимости
RUN pip3 install -r /catkin_ws/src/my_robot_project/requirements.txt

# Собираем проект
WORKDIR /catkin_ws
RUN catkin_make

# Запускаем основной скрипт
CMD ["python3", "/catkin_ws/src/my_robot_project/src/main.py"]
