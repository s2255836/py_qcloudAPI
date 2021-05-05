from my_models.config import cred, args
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception \
    import TencentCloudSDKException
from tencentcloud.ecdn.v20191012 import ecdn_client, models  # noqa
import json

httpProfile = HttpProfile()
httpProfile.endpoint = "ecdn.tencentcloudapi.com"
clientProfile = ClientProfile()
clientProfile.httpProfile = httpProfile
client = ecdn_client.EcdnClient(cred, "", clientProfile)


def example(params):
    try:
        req = eval('models.' + args.m + 'EcdnDomainRequest()')
        req.from_json_string(json.dumps(params))
        resp = eval('client.'+args.m + 'EcdnDomain' + '(req)')
        print(resp.to_json_string())
    except TencentCloudSDKException as err:
        print(err)


class Ecdn_base():

    def addEcdn(self, port, ssl, pri, pub):
        """ Qcloud SDK生成後加入自訂變數"""
        params = {
            "Domain": self,
            "Origin": {
                "Origins": port,
                "OriginType": "ip",
                "OriginPullProtocol": "http"
            },
            "ProjectId": 0,
            "Https": {
                "Switch": ssl,
                "CertInfo": {
                    "PrivateKey": pri,
                    "Certificate": pub
                }
            },
            "Area": "global"
        }
        example(params)

    def stopEcdn(self):
        params = {
            "Domain": self
        }
        example(params)
