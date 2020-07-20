# 初次设置
1. 每次启动都要切换到root用户：
    ```bash
    sudo -i
    ```
2. 安装wget：
    ```bash
    yum install -y wget
    ```
3. 一键开启bbr加速：
    ```bash
    wget "https://github.com/cx9208/bbrplus/raw/master/ok_bbrplus_centos.sh" && chmod +x ok_bbrplus_centos.sh && ./ok_bbrplus_centos.sh
    ```
4. 检查bbrplus是否开启成功，执行以下语句，显示有bbrplus则表示加速开启成功：
    ```bash
    lsmod | grep bbr 
    ```
5. 一键安装Shadowsocks：
    ```bash
    wget --no-check-certificate -O shadowsocks-all.sh https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowsocks-all.sh && chmod +x shadowsocks-all.sh && ./shadowsocks-all.sh 2>&1 | tee shadowsocks-all.log
    ```
6. 选择想要安装的shadowsocks后，对每一个选择都按Enter键，等待安装完成打印提示信息。
7. 查看SSR状态，执行以下语句，显示is running
    ```bash
    /etc/init.d/shadowsocks-r status
    ```
8. 将打印出来的ssr链接配置至本地

notes: 
- SSR启动 | 停止 | 重启 | 查看状态：
```bash
/etc/init.d/shadowsocks-r start | stop | restart | status
```
- SSR配置文件路径：
```bash
/etc/shadowsocks-r/config.json
```
 
# FAQ
## 服务器上能ping通youtube而本地不行
### for shadowsocks
1. `cd /etc/shadowsocks-python;sudo vi config.json`
2. reset a new port
3. `sudo ssserver -c config.json -d restart`
