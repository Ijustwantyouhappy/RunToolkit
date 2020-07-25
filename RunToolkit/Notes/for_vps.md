# SS & SSR
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
5. 一键安装SS或者SSR等：
    ```bash
    wget --no-check-certificate -O shadowsocks-all.sh https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowsocks-all.sh && chmod +x shadowsocks-all.sh && ./shadowsocks-all.sh 2>&1 | tee shadowsocks-all.log
    ```
6. 选择想要安装的shadowsocks后，对每一个选择都按Enter键，等待安装完成打印提示信息。
7. 查看SSR状态，执行以下语句，显示is running
    ```bash
    /etc/init.d/shadowsocks-r status
    ```
8. 将打印出来的ssr链接配置至本地

**notes**:
- SSR启动 | 停止 | 重启 | 查看状态：
```bash
/etc/init.d/shadowsocks-r start | stop | restart | status
```
- SSR配置文件路径：
```bash
/etc/shadowsocks-r/config.json
```
- 查找含有"shadowsocks"的所有程序
```bash
ps -aux | grep shadowsocks
```
 
# [V2Ray](https://hijk.pp.ua/v2ray-one-click-script-with-mask/)
1. [购买域名并设置主机名](https://hijk.pp.ua/namesilo-buy-domain-tutorial/)
2. 一键安装V2Ray（含伪装、bbr加速），按提示进行输入即可
```bash
bash <(curl -sL https://raw.githubusercontent.com/hijkpw/scripts/master/centos_install_v2ray2.sh)
```

**notes**:
- 判断服务端是否已经正常运行：浏览器输入域名，打开应该是一个随机小说网站。
- 查看v2ray运行状态/配置：
```bash
bash <(curl -sL https://raw.githubusercontent.com/hijkpw/scripts/master/centos_install_v2ray2.sh) info
```
- v2ray 启动/停止/重启：
```bash
systemctl start | stop | restart v2ray
```
- nginx 启动/停止/重启：
```bash
systemctl start | stop | restart nginx
```
- 更新v2ray到最新版：
```bash
bash <(curl -L -s https://install.direct/go.sh)
```
- 卸载v2ray： 
```bash
bash <(curl -sL https://raw.githubusercontent.com/hijkpw/scripts/master/centos_install_v2ray2.sh) uninstall
```


# FAQ
## 服务器上能ping通youtube而本地不行
### for shadowsocks
1. `cd /etc/shadowsocks-python;sudo vi config.json`
2. reset a new port
3. `sudo ssserver -c config.json -d restart`
