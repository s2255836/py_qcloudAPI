from cloudapi.env import HttpProfile, ClientProfile, cred, args, json

# 刷新CDN
def cdn():
    from tencentcloud.cdn.v20180606 import cdn_client, models
    CDN_list = args.url.split(',')
    httpProfile = HttpProfile()
    httpProfile.endpoint = "cdn.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = cdn_client.CdnClient(cred, "", clientProfile)

    req = models.PurgePathCacheRequest()
    params = {
        "Paths": CDN_list,
        "FlushType": args.fresh
    }
    req.from_json_string(json.dumps(params))

    resp = client.PurgePathCache(req)
    print(resp.to_json_string())
