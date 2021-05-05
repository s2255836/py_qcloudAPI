import requests
import json
import pandas as pd

url = 'http://certchecker:8080/domain'


class sslApi():

    @staticmethod
    def gethost():
        r = requests.get(url)
        data = pd.DataFrame()
        for i in range(len(json.loads(r.text))):
            append_df = pd.DataFrame(json.loads(r.text)[i], index=[0])
            data = data.append(append_df)
            data.index = data.id
        return data

    def posthost(name, host):
        my_data = {
            "name": name,
            "host": host
        }
        p = requests.post(url, data=json.dumps(my_data))
        if p.status_code == 201:
            print("Post certchecker Success")
        else:
            print("""Already in or Other problems,
                    Please check your domain on certchecker""")

    def deletehost(host):
        data = sslApi.gethost()
        id_list = data[data.host.str.contains(host)].index.to_list()
        if id_list:
            for id in id_list:
                delurl = url + '/' + str(id)
                d = requests.delete(delurl)
                if d.status_code == 204:
                    print("Deleted Success on certchecker")
                else:
                    print("Somthing Wrong, please tell the maintainer")
        else:
            print("No such domain or has been Deleted")
