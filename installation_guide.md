# Ставим Ubuntu
 1. Образ 64-bit PC (ubuntu-16.04.5-desktop-amd64.iso) отсюда http://releases.ubuntu.com/16.04/
 2. Не меньше 32 Gb Swap

# Установка пакетов
 1. Обновляем индекс пакетов ```sudo apt-get update```
 2. ```sudo apt-get install -y build-essential curl software-properties-common libssl-dev libffi-dev ssh gnupg-curl tmux git mc python-dev python-pip python3-dev python3-pip at pwgen htop iotop iftop tcpdump libbz2-dev netcat-traditional telnet vim-nox```
 3. ```sudo apt install python-virtualenv python3.5-venv bison automake libpcre3-dev libpcre++-dev```
 4. ```sudo pip install pip setuptools --upgrade```
 5. ```sudo pip install numpy psutil```

# Установка Python3.6
 1. ```sudo add-apt-repository ppa:deadsnakes/ppa```
 2. ```sudo apt-get update```
 3. ```sudo apt-get install python3.6```
 4. ```sudo apt-get install python3.6-venv```

# Установка библиотек
 1. python[2,3.5,3.6] -m pip install -U --user setuptools pip
 2. python[2,3.5,3.6] -m pip install --user scipy numpy matplotlib pandas sklearn tqdm mkl numpy nltk pyasn1 ndg-httpsclient scikit-image pyopenssl
 3. ставим Jupyter: ```pip3 install --user jupyter```
 4. ставим kernel-ы: 
    * python[2,3.5,3.6] -m pip install --user ipykernel
    * sudo python[2,3.6] -m ipykernel install
 5. устанавливаем самые свежие Theano, Lasagne, Keras на все версии Python: python[2,3.5,3.6] -m pip install --user --upgrade https://github.com/Theano/Theano/archive/master.zip https://github.com/Lasagne/Lasagne/archive/master.zip keras


