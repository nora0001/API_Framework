import  requests
from Hogwarts_API_Test.api import BaseApi
import pytest

class ApiHttpbinGet(BaseApi):
    url = "http://httpbin.org/get"
    method="GET"
    params={}
    headers={"accept":"application/json"}
    json={}
    data=""


class ApiHttpbinPost(BaseApi):
    url = "http://httpbin.org/post"
    method = "POST"
    params={}
    headers = {"accept": "application/json"}
    json = {}
    data=""


class Test_api():
    def test_httpbin_get(self):

        #级联调用
        ApiHttpbinGet().run()\
            .validate("status_code",200)\
            .validate("headers.Server","gunicorn/19.9.0")\
            .validate("json().url","http://httpbin.org/get")\
            .validate("json().args",{})\
            .validate("json().headers.Accept", 'application/json')

    def test_httpbin_get_with_params(self):

        params = {"abc": 123,"xyz": 456}
        ApiHttpbinGet().set_params(params).run()\
            .validate("status_code",200)\
            .validate("headers.Server","gunicorn/19.9.0")\
            .validate("json().url","http://httpbin.org/get?abc=123&xyz=456")\
            .validate("json().args",{'abc': '123', 'xyz': '456'})\
            .validate("json().headers.Accept", 'application/json')


    def test_httpbin_post(self):
        json ={"abc":123}
        ApiHttpbinPost().set_params(json).run()\
            .validate("status_code",200)\
            .validate("headers.Server", "gunicorn/19.9.0") \
            .validate("json().url", "http://httpbin.org/post?abc=123") \
            .validate("json().args", {'abc': '123'}) \
            .validate("json().headers.Accept", 'application/json')



