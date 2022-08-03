# Запуск программы на Ubuntu вызывает ошибку со звуком. Для решения проблемы на Ubuntu следует сделать следующее:
# sudo apt-get install freepats
# sudo apt-get install timidity
# Больше информации тут: https://medium.com/@karthik_ak/pygame-midi-file-issue-on-ubuntu-16-04-2dcfc776ede9

from asyncore import loop
from superwires import games

games.init(screen_width=640, screen_height=480, fps=50)

missile_sound = games.load_sound("chapter_12/missile.wav")
games.music.load("chapter_12/theme.mid")
choice = None
while choice != "0":
    print(
        '''
        Sound and music
        0 - Exit
        1 - Play sound of missile
        2 - Repeat sound of missile
        3 - Stop sound of missile
        4 - Play music theme
        5 - Repeat music theme
        6 - Stop music theme
        '''
    )

    choice = input("Your choice: ")
    print()
    if choice == "0":
        print("Bye")
    elif choice == "1":
        missile_sound.play()
        print("Playing sound of missile")
    elif choice == "2":
        loop = int(input("Times repeat: "))
        missile_sound.play(loop)
        print("Repeating sound of missile")
    elif choice == "3":
        missile_sound.stop()
        print("Stoping sound")
    elif choice == "4":
        games.music.play()
        print("Playing music")
    elif choice == "5":
        loop = int(input("Times repeat: "))
        games.music.play(loop)
        print("Repeat playing music")
    elif choice == "6":
        games.music.stop()
        print("Stop music")
    else:
        print("Sorry. There's no such choice")

input("\n\nPress Enter to Exit.")

        

