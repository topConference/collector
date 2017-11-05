# conference collector

collect conference data from http://www.guide2research.com/
mongodb & mysql support

## install

1. install crontab(archlinux)

    ```sh
    sudo pacman -S --needed cronie
    sudo systemctl start cronie
    ```
    install crontab(centos7)
    ```sh
    systemctl start crond
    ```
2. install dependency(centos7)

    ```sh
    sudo yum -y install https://centos7.iuscommunity.org/ius-release.rpm
    sudo yum -y install python36u python36u-pip python36u-devel
    sudo pip3.6 install --upgrade mysqlclient scrapy
    ```
    
## usage

1. change usr, passwd and pipline in `settings.py`

2. if using mysql, create database and table refer to `create.sql`

3. collect one time

    ```sh
    python main.py
    #centos7
    python3.6 main.py
    ```
    
4. update every day

    ```sh
    01 01 * * * python /home/root/top/main.py
    ```

## reference

[crontab](http://linuxtools-rst.readthedocs.io/zh_CN/latest/tool/crontab.html)

[archwiki](https://wiki.archlinux.org/index.php/Cron_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87))

