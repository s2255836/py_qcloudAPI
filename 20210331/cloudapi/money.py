from cloudapi.env import HttpProfile, ClientProfile, cred, args, json
from tencentcloud.billing.v20180709 import billing_client, models


def bill():
    httpProfile = HttpProfile()
    httpProfile.endpoint = "billing.tencentcloudapi.com"

    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = billing_client.BillingClient(cred, "", clientProfile)

    req = models.DescribeBillSummaryByProductRequest()
    params = {
        "BeginTime": args.time,
        "EndTime": args.time
    }
    req.from_json_string(json.dumps(params))
    resp = client.DescribeBillSummaryByProduct(req)
    listnum = len(resp.SummaryOverview)
    for list_item in range(listnum):
        overview = json.loads(str(resp.SummaryOverview[list_item]))
        print("\n")
        for project, value in overview.items():
            print(project, ":", value)
    total = json.loads(str(resp.SummaryTotal))
    print("\n", "TOTAL COST:", sep="")
    for project, value in total.items():
        print(project, ":", value)

# 拿帳戶餘額


def money():
    httpProfile = HttpProfile()
    httpProfile.endpoint = "billing.tencentcloudapi.com"
    clientProfile = ClientProfile()
    clientProfile.httpProfile = httpProfile
    client = billing_client.BillingClient(cred, "", clientProfile)
    req = models.DescribeAccountBalanceRequest()
    params = {
    }
    req.from_json_string(json.dumps(params))
    resp = client.DescribeAccountBalance(req)
    m_respon = float(json.loads(resp.to_json_string())['Balance'])/100
    print(m_respon)
