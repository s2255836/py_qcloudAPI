from cloudapi.env import HttpProfile, ClientProfile, cred, args, json


# 刷新全球加速
def dcdn():
    from tencentcloud.ecdn.v20191012 import ecdn_client, models
    DCDN_list = args.url.split(',')
    httpProfile = HttpProfile()
    httpProfile.endpoint = "ecdn.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = ecdn_client.EcdnClient(cred, "", clientProfile)

    req = models.PurgePathCacheRequest()
    params = {
        "Paths": DCDN_list,
        "FlushType": args.fresh
    }
    req.from_json_string(json.dumps(params))

    resp = client.PurgePathCache(req)
    print(resp.to_json_string())
