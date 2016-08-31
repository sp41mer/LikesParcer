__author__ = 'sp41mer'
import requests, json, time
import require_info

vk_access_token = require_info.vk_access_token
method = "likes.getList"
type = "post"
url = "https://m.vk.com/wall-58656979_27636"

fields = require_info.fields

def chunks(l, n):
    """Yield successive n-sized chunks from l."""
    for i in range(0, len(l), n):
        yield l[i:i + n]

owner_id = "-58656979"
item_id = "7509"
extended = 0
offset = 0
count = 1000
version = "5.53"

response = requests.post('https://api.vk.com/method/' + method,
                                data={'type': type,
                                      'owner_id': owner_id,
                                      'item_id': item_id,
                                      'offset': offset,
                                      'count' : count,
                                      'v': 5.53,
                                      'access_token': vk_access_token})
data = json.loads(response.text)
volume = data['response']['count']
ids_array = data['response']['items']
if volume > 1000:
    ids_array = data['response']['items']
    for i in range(1, (volume//1000 + 1)):
        offset += 1000
        response = requests.post('https://api.vk.com/method/' + method,
                                data={'type': type,
                                      'owner_id': owner_id,
                                      'item_id': item_id,
                                      'offset': offset,
                                      'count': count,
                                      'v': 5.53,
                                      'access_token': vk_access_token})
        data = json.loads(response.text)
        ids_array = ids_array +(data['response']['items'])
        time.sleep(0.4)

ids_array = list(chunks(ids_array,999))
for user_group in ids_array:
    method = "users.get"
    response = requests.post('https://api.vk.com/method/' + method,
                             data={'user_ids': user_group,
                                   'fields': fields,
                                   'v': 5.53,
                                   'access_token': vk_access_token})

