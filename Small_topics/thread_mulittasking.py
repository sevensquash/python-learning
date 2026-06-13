# threading is useful for mulitasking performing mulitple task concurrently 
# very useful for I/O bound task like reading and fetching data from API

from threading import Thread
from time import sleep 

def eat_chip():
    sleep(2)
    print("You just ate chip")

def write():
    sleep(6)
    print("You just wrote something")

def drink_water():
    sleep(5)
    print("You just drank water")

def play_music(music):
    sleep(8)
    print(f"You just put on msuic: {music}")

chore1 = Thread(target=eat_chip)
chore1.start()
chore2 = Thread(target=write)
chore2.start()
chore3 = Thread(target=drink_water)
chore3.start()
# args send argument as tuple and that , is necessary
chore4 = Thread(target=play_music, args=("Rufus",))
chore4.start()

chore1.join()
chore2.join()
chore3.join()
chore4.join()

print("All task is done. Now go study!")