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
        actual_value = getattr(self.response, key)
        assert actual_value == expected_value
        return self
