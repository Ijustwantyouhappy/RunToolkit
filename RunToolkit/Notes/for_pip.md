# 强行更新
```bash
python -m pip install --user --ignore-installed --upgrade numpy
```

# 下载和离线安装
下载：
```bash
pip download -d 路径 包名
```
离线安装：
```bash
pip install --no-index --find-links=路径 包名
```
该方式多用于向一台没有连网的服务器安装包，需要保证下载和离线安装的两个环境的系统和python版本一致。