<font color="red">������״ζԸ���Ŀ���У���Ҫ�Ӳ���1��ʼ�����֮ǰ�Ѿ��Ը���Ŀ�ύ��pr������ֱ�ӴӲ���5��ʼ��</font>

1. fork����Ŀ��ֿ⣨����x��forkΪ�Լ��Ĳֿ⣨����y�����ڲֿ���ҳ�����Ͻǵ��Fork��ť���ɡ�
2. clone����y�ֿ�clone�����ء�
3. �������ӣ�
    ```bash
    git remote add upstream x����ĿԴ
    ```
4. �鿴�����Ƿ�ɹ����ɹ�����ʾoriginΪy����ĿԴ��upstreamΪx����ĿԴ���������ʾǰ�ߡ�
    ```bash
    git remote -v
    ```
5. ������֧��pycharm�п��������½�ͨ��ͼ�ν��������
    ```bash
    git checkout -b XXX
    ```
6. ��Ŀ�������иĶ�
7. ���Ķ��ύ��y��ύ֮ǰҪע������xͬ����
    ```bash
    git fetch upstream
    git merge upstream/master  
    git push origin master
    ```
8. �ύPR����y��Ŀ����ҳ���в��������Pull Request��д��Ϣ��
9. �ȴ�x��Ŀά����Ա��ˣ����ύ��PR��merge�󣬻����һ��ɾ������Ŀ�з�֧�Ĳ�����������У�ͨ��ѡ��ɾ�������صķ�֧Ҳ����ɾ��������