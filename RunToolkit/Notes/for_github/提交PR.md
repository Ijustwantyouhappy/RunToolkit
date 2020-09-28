<font color="red">如果是首次对该项目进行，需要从步骤1开始，如果之前已经对该项目提交过pr，可以直接从步骤5开始。</font>

1. fork：将目标仓库（记作x）fork为自己的仓库（记作y），在仓库首页的右上角点击Fork按钮即可。
2. clone：将y仓库clone到本地。
3. 建立连接：
    ```bash
    git remote add upstream x的项目源
    ```
4. 查看连接是否成功：成功会显示origin为y的项目源，upstream为x的项目源，否则仅显示前者。
    ```bash
    git remote -v
    ```
5. 创建分支：pycharm中可以在右下角通过图形界面操作。
    ```bash
    git checkout -b XXX
    ```
6. 对目标代码进行改动
7. 将改动提交到y里（提交之前要注意先与x同步）
    ```bash
    git fetch upstream
    git merge upstream/master  
    git push origin master
    ```
8. 提交PR：在y项目的主页进行操作，点击Pull Request填写信息。
9. 等待x项目维护人员审核：当提交的PR被merge后，会给出一个删除你项目中分支的操作，按需进行（通常选择删除，本地的分支也可以删除掉）。