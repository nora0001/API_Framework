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
            if isinstance(value,requests.Response):
                value = getattr(value,_key)
            elif isinstance(value,requests.structures.CaseInsensitiveDict):
                value = value[_key]


        assert value == expected_value
        return self
