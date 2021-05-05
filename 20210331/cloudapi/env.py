import json
import configparser
import argparse
from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
# 讀配置
config = configparser.ConfigParser()
config.read('config.ini')

# 定義命令參數
parser = argparse.ArgumentParser(description='看看怎麼用')
parser.add_argument('-user', help='必須, 帳號: q-177 , qpitoper , us9base')
parser.add_argument(
    '-method', help='必須, 帳單:bill , 餘額:money, CDN刷新:CDN, DCDN刷新:DCDN')
parser.add_argument(
    '-time', help='bill選用, -method bill 才使用此參數,example: 2020-12')
parser.add_argument('-fresh', default="flush",
                    help='CDN選用, flush:刷新變更資源, delete:刷新全部資源')
parser.add_argument('-url', help='CDN選用, CDN, 帶https/http域名')

# global config
args = parser.parse_args()


def user_set():
    if args.user is None:
        print("沒帳號是要查三小, 看一下-h好嗎?")
        exit()
    elif args.user not in config.sections():
        print("請在config,ini中新增user")
        exit()


user_set()

cred = credential.Credential(
    config[args.user]['SecretID'], config[args.user]['Secretkey'])
