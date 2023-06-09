import os
import json

from googleapiclient.discovery import build




class Channel:
    """Класс для ютуб-канала"""
    api_key: str = os.getenv('YT_API_KEY')
    youtube = build('youtube', 'v3', developerKey=api_key)


    def __init__(self, channel_id: str):
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        channel = self.youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

        self.__channel_id = channel_id
        self.title = channel['items'][0]['snippet']['title']
        self.url = f'https://www.youtube.com/channel/{channel_id}'
        self.count_subscribers = channel['items'][0]['statistics']['subscriberCount']
        self.video_count = channel['items'][0]['statistics']['videoCount']
        self.view_count = channel['items'][0]['statistics']['viewCount']


    def print_info(self):
        """Выводит в консоль информацию о канале."""
        print(json.dumps(self.youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute(),
                         indent=2, ensure_ascii=False))

    @classmethod
    def get_service(cls) -> build:
        """Возвращающий объект для работы с YouTube API"""
        return build('youtube', 'v3', developerKey=cls.api_key)

    @property
    def channel_id(self) -> str:
        """Геттер для id канала"""
        return self.__channel_id

    def to_json(self, filename) -> None:
        """метод, который сохраняет в файл значения атрибутов экземпляра Channel"""
        with open(filename, "w") as f:
            json.dump(self.__dict__, f, indent=2)


