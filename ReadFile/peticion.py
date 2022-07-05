import requests
import json


class Request:

    def requestEndPoint(self):
        try:
            self.filename = "archivos/Clientes.txt"

            with open(self.filename, encoding="utf-8") as file:
                for line in file:
                    self.dataf = line.strip().split(',')
                    self.client_data ={
                        "firtsName": self.dataf[0],
                        "surname": self.dataf[1],
                        "country": {
                            "name": self.dataf[2],
                            "airports": [
                                {
                                    "name": self.dataf[4]
                                }
                            ]
                        },
                        "spokenLanguages": [
                            {
                                "name": self.dataf[3]
                            }
                        ]
                    }
                    json_object = json.dumps(self.client_data, indent = 4)

                    hdr = {"Content-Type": "application/json"}

                    response = requests.post('http://localhost:8080/test/apiv1/clientes/add', data=json_object, headers=hdr)
                    
                    # print(response.request.body)
                    # print(response.status_code)
                    
            if response.status_code == 200:
                print('Success!')
            elif response.status_code == 404:
                print('Not Found.')
        except Exception as e:
            print(e)


resp = Request()
resp.requestEndPoint()
