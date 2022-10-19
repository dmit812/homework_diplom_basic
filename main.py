from vk_import import VkImport

from yandex import YaUploader


if __name__ == '__main__':
    with open('token.txt', 'r') as file_object:
        token_vk = file_object.read().strip()

    id_vk = input('Введите id пользователя vk: ')
    vk_import = VkImport(token_vk, '5.131')
    vk_import.sorting_foto(vk_import.get_photos(id_vk))

    token_ya = input('Введите токен с полигона Яндекс диска: ')
    yandex = YaUploader(token_ya)
    yandex.get_create_folder()
    yandex.get_upload_file(vk_import.get_photos(id_vk))
