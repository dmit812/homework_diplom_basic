import requests

from tqdm import tqdm

from time import sleep


class YaUploader:

    def __init__(self, token_ya):
        self.token_ya = token_ya

    def _create_header(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token_ya)
        }

    def get_create_folder(self):
        url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self._create_header()
        params = {'path': 'VK_Photo', "overwrite": "true"}
        response = requests.put(url, headers=headers, params=params)

    def get_upload_file(self, file_list):
        pbar = tqdm(total=len(file_list))
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self._create_header()
        for inf, photo in enumerate(file_list):
            sleep(0.1)
            pbar.update(1)
            file_name = '_'.join([str(inf + 1), str(photo['likes']['count'])])
            path = f'VK_Photo/{file_name}.jpeg'
            params = {'path': path, 'url': photo['sizes'][-1]['url']}
            response = requests.post(url, headers=headers, params=params)
            response.raise_for_status()
        pbar.close()
        if response.status_code == 202:
            print('Фотографии успешно загружены.')
