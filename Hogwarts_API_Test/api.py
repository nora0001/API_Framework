import requests


class BaseApi(object):
    url = ""
    method=""
    params={}
    headers={"accept":"application/json"}
    data=""
    json={}

    def set_params(self, params):
        self.params = params
        return self

    def run(self):
        self.response= requests.request(self.method,
                                        self.url,
                                        headers=self.headers,
                                        params=self.params,
                                        json=self.json,
                                        data=self.data
                                    )
        return self

    def validate(self, key, expected_value):
        value=self.response
        for _key in key.split("."):
            print("======",_key, value, type(value))
            if isinstance(value,requests.Response):
                if _key == "json()":
                    value = self.response.json()
                else:
                    value = getattr(value,_key)
            elif isinstance(value,(requests.structures.CaseInsensitiveDict,dict)):
                value = value[_key]

        print("======2222", _key, value, expected_value)


        assert value == expected_value
        return self
