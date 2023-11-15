import time
import pygame

def alarm_sesi_cal():
    pygame.mixer.init()
    pygame.mixer.music.load("alarm_sesi.mp3")  # "alarm_sesi.mp3" kısmını kendi ses dosyanızın yoluna değiştirin
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

def alarm_kur(alarm_saati):
    while True:
        suanki_zaman = time.strftime("%H:%M:%S")
        if suanki_zaman == alarm_saati:
            print("Uyanma zamanı!")
            alarm_sesi_cal()
            break
        else:
            print(f"Mevcut zaman: {suanki_zaman}. {alarm_saati} bekleniyor.")
            time.sleep(1)

if __name__ == "__main__":
    alarm_saati = input("Alarm saati (HH:MM:SS formatında) girin: ")
    alarm_kur(alarm_saati)
