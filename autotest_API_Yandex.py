import pytest
import requests
from decouple import config


class TestYandexDisk:

    def setup_method(self):
        self.headers = {
            'Authorization': f'OAuth {config("token",default="")}'
        }
        self.url = 'https://cloud-api.yandex.net/v1/disk/resources?'

    @pytest.mark.parametrize(
        'path, status',
        (['new_test_folder', 201],
         ['new_test_folder', 409])
    )
    def test_create_folder(self, path, status):
        response = requests.put(f'{self.url}path={path}',
                                headers=self.headers)
        assert response.status_code == status
