
import Video
from User import *
from Video import *
class UrTube:
    list_us_name = []
    def __init__(self, users = User.list_user, videos = Video.list_video, current_user = User.list_user[0]):
        self.users = users
        self.videos = videos
        self.current_user = current_user

    def log_in(self,nickname, password):
        for i in User.list_user:
            if i == nickname:
                self.current_user = i

    def register(self, nickname, password, age):
        self.nickname = nickname
        for uuu in User.list_user:
            for geg in UrTube.list_us_name:
                if geg == uuu:
                    "такой пользователь уже есть "
                else:
                    UrTube.list_us_name.append(geg)
                    return

    def log_out(self):
        self.current_user = None

    def add(self, *video):
        if Video.list_video in video:
            print(" ")
        else:
            Video.list_video.append(video)

    def get_videos(self, text):
        text1 = str(text).lower()
        for k in Video.list_video :
            fff = k.lower()
            if fff == text:
                return
            else:
                return

    def watch_video(self, film):
        for tyu in Video.list_video:
            if film == tyu:
                if film == BID2.title:
                    print(BID2.title, BID2.duration, BID2.time_now)
                else:
                    print(" ")

                if film == BID.title:
                    print(BID.title, BID.duration, BID.time_now)
                else:
                    print(" ")

                if film == BID3.title:
                    print(BID3.title, BID3.duration, BID3.time_now)
                else:
                    print(" ")
            else:
                print(" ")
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
