# conference collector

collect conference data from http://www.guide2research.com/

## install

1. install crontab(archlinux)

    ```sh
    sudo pacman -S --needed cronie
    sudo systemctl start cronie
    ```
    
2. install dependency

    ```sh
    sudo pip install --upgrade mysqlclient scrapy
    ```
## usage

1. change mysql usr and passwd in `settings.py`

2. create database and table refer to `create.sql`

3. collect one time

    ```sh
    python main.py
    ```
    
4. update every day

    ```sh
    01 01 * * * python /home/root/top/main.py
    ```

## reference
[crontab](http://linuxtools-rst.readthedocs.io/zh_CN/latest/tool/crontab.html)

[archwiki](https://wiki.archlinux.org/index.php/Cron_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))

