# jupyter服务器只能下载单个文件
解决方案：打包文件夹到单个文件后再下载
- `tar`（注：tar是打包，不是压缩！）
    * 解包：`tar xvf FileName.tar`
    * 打包：`tar cvf FileName.tar DirName`
- `tar.gz`
    * 解压：`tar zxvf FileName.tar.gz`
    * 压缩：`tar zcvf FileName.tar.gz DirName`