class Camera:
    def take_photo(self):
        print("Taking a photo")


class MusicPlayer:
    def play_music(self):
        print("Playing music")


# Herencia múltiple
class SmartPhone(Camera, MusicPlayer):
    def make_call(self):
        print("Making a call")


# Crear objeto
phone = SmartPhone()

# Usar métodos heredados
phone.take_photo()
phone.play_music()
phone.make_call()