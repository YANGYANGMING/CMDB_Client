import requests
import time
import hashlib

host_data = {'status': True,
            'message': None,
            'data': {'os_platform': 'linux',
                      'os_version': 'CentOS release 6.6',
                      'hostname': 'c1.com',
                      'cpu': {'status': True,
                               'message': None,
                               'data': 'xxoo',
                               'error': None},
                      },
            'error': None}

# requests.get(url='http://127.0.0.1:8000/api/asset?k1=123')
# requests.get(url='http://127.0.0.1:8000/api/asset', params={'k1': 123})
#
# requests.post(
#     url='http://127.0.0.1:8000/api/assets',
#     json=host_data,  #把字段json序列化，传到body中
# )


current_time = time.time()

app_id = 'qwewrweefasfd'
app_id_time = '%s|%s' % (app_id, current_time)

m = hashlib.md5()
m.update(bytes(app_id_time, encoding='utf8'))
authkey = m.hexdigest()

authkey_time = '%s|%s' % (authkey, current_time)
print(authkey_time)  #e05669e941eafd7329e3133dfcef41e6|1561643115.3727212

response = requests.post(
    url='http://127.0.0.1:8000/api/asset/',
    # params={'k1': 'v1'},  #get方式发送
    # data=host_data,  #post方式
    json=host_data,
    headers={'authkey': authkey_time}  #请求头数据
)

print(response.text)






