# 服务器上能ping通youtube而本地不行
解决方案：重设shadowsocks的port
1. `cd /etc/shadowsocks-python`
2. `sudo vi config.json`
3. reset a new port
4. `sudo ssserver -c config.json -d restart`