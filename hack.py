import requests


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


response = requests.post(
    url='http://127.0.0.1:8000/api/asset/',
    # params={'k1': 'v1'},  #get方式发送
    # data=host_data,  #post方式
    json=host_data,
    headers={'authkey': '92ef0c13c96440721fc60e650054ae28|1561647150.36548'}  #请求头数据
)

print(response.text)