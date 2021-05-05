from tencentcloud.common import credential
import configparser
import argparse
# 配置
config = configparser.ConfigParser()
config.read('config.ini')

# 定義命令參數
parser = argparse.ArgumentParser(description='doc')

parser.add_argument('-user', required=True,
                    help='必須, 帳號:  ...etc')

parser.add_argument('-d', required=True, help='主域名')

parser.add_argument('-n', required=False, help='域名用處,用在certchecker')

parser.add_argument('-f', required=True, help='域名列表: json格式檔案')

parser.add_argument('-ssl', choices=["on", "off"],
                    required=False, default="off", help='是否使用憑證')

parser.add_argument('-m', choices=["Add", "Stop", "Delete"],
                    required=True, default="add", help='Main function')


# 命令行參數成為變數 args.user, args.d, args.ssl
args = parser.parse_args()

if args.user not in config.sections():
    print("請在config.ini中新增user")
    exit()

# 從config.ini讀取帳號token
cred = credential.Credential(
    config[args.user]['SecretID'], config[args.user]['Secretkey'])


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
