import requests

import json


class VkImport:
    url = 'https://api.vk.com/method/'

    def __init__(self, token_vk, version):
        self.params = {
            'access_token': token_vk,
            'v': version
        }

    def get_photos(self, id_vk):
        url_photo_get = self.url + 'photos.get'
        params_photo_get = {
            'owner_id': id_vk,
            'album_id': 'profile',
            'extended': 1,
            'photo_sizes': 1,
            'count': 5
        }
        res = requests.get(url_photo_get, params={**self.params, **params_photo_get}).json()
        return res['response']['items']

    def sorting_foto(self, listing):
        photo_res = []
        for inf, photo in enumerate(listing):
            photo_res.append({
                'file_name': '_'.join([str(inf + 1), str(photo['likes']['count'])]),
                'size': photo['sizes'][-1]['type']
            })
        best_photos = json.dumps(photo_res)
        with open("best_photo.json", "w") as filejson:
            filejson.write(best_photos)
