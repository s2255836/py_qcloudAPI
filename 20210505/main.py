from my_models.config import args, config, bcolors  # noqa
from my_models.ecdn import Ecdn_base as ecdn
from my_models.cerchecker import sslApi  # noqa
import os
import json


def SSLwrite():
    """Jenkins帶入pem資料,寫進檔案 檔案名稱固定,
    統一做法,避免其他問題"""
    file = {"sslpub": "fullchain.pem", "sslpri": "privkey.pem"}
    for ssl, filename in file.items():
        jenkins_var = os.getenv(ssl)
        fp = open(filename, 'w')
        fp.write(jenkins_var)
        fp.close


# -ssl "on":讀取證書檔案,否則為空值
if args.ssl == 'on':
    SSLwrite()
    with open("fullchain.pem", "r", encoding="utf-8") as sslpub:
        global pub
        pub = sslpub.read()
        sslpub.close()
    with open("privkey.pem", "r", encoding="utf-8") as sslpri:
        global pri
        pri = sslpri.read()
        sslpri.close()
else:
    pri = ""
    pub = ""

# 查看創建domain列表
with open(args.f, "r", encoding="utf-8") as domain:
    data = json.load(domain)
    domain.close()

# 處理json字串
for domain, port in data['domain'].items():
    mydomain = str(domain + '.' + args.d)
    myip = []
    print(bcolors.OKBLUE + args.m + " --> " + mydomain + bcolors.ENDC)
    if domain == 'h5mms':
        myip += [str(data['ip']['mms'] + ':' + port)]
    else:
        for ip in data['ip']['small'].split(','):
            myip += [str(ip + ':' + port)]
    if args.m == 'Add':
        ecdn.addEcdn(mydomain, myip, args.ssl, pri, pub)
        host = mydomain + ':443'
        certcheck = sslApi.posthost(args.n, host)
    else:
        ecdn.stopEcdn(mydomain)
        sslApi.deletehost(mydomain)
