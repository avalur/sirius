# Установка Oracle VB
1. Ставим virtual box https://www.virtualbox.org/wiki/Downloads (for windows hosts у меня)
2. Для появления x64-систем (host windows 10) отключил изоляцию ядра, как сказано тут (https://forums.virtualbox.org/viewtopic.php?t=62339), помогла команда 
dism.exe /Online /Disable-Feature:Microsoft-Hyper-V 
отсюда https://superuser.com/questions/1153470/vt-x-is-not-available-but-is-enabled-in-bios

# Установка Ubuntu на неё
3. Скачиваем образ ubuntu-16.04.5-desktop-amd64.iso отсюда http://releases.ubuntu.com/16.04/ и устанавливаем

# Доделки (уже мелкие)
4. VirtualBox -> Devices -> Insert Guest Additions CD image
5. Then Ubuntu -> Settings -> Advanced and Bidirectional (clipboard and drag and drop) 
6. Ubuntu -> Settings -> Shared Folders -> +folder (automount /home/avalur/share)
7. Ещё в Ubuntu (guest) настраиваем никогда не блокировать экран.
8. 
