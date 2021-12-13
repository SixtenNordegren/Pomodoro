import time
import os
from pydub import AudioSegment
from pydub.playback import play
import datetime
import numpy as np

bell = AudioSegment.from_wav("bell.wav")

def time_converter(sec):
    minutes = sec // 60
    sec = sec % 60
    hours = minutes // 60
    minutes = minutes % 60
    output = "Time lapsed = {0}:{1}:{2}".format(
            int(hours),
            int(minutes),
            int(sec)
            )
    return output

def output_style(item, count, message):
    os.system("clear")
    print("               ", message)
    print("                                    ", count)
    print("\n \n \n \n")
    print("               ", item)

def start_clock(length, count, message):
    start_time = time.time()
    waited = 0
    while waited < length:
        waited = time.time() - start_time
        output_style(time_converter(waited), count, message)
        time.sleep(1)

def completed(count):
    print(
            "Congratulations you finished your pomodoro number {0}".format(
                count))
    play(bell)

def savefile(count, date_time):

    log_string = str(count) + "," + str(date_time)

    file = open("log.txt","a")
    file.write("\n" + log_string)
    file.close()

def readfile(date_time):
    read = np.loadtxt("log.txt", delimiter=",", dtype="int")
    if int(read[-1][1]) == int(date_time):
        return int(read[-1][0])
    else:
        return 0

def main():
    ct = datetime.datetime.now()
    date_time = str(ct.year) + str(ct.month) +str(ct.day)

    rest_time = 5*60**2
    work_time = 25*60**2

    interrupt = False

    count = readfile(date_time)

    while interrupt == False:
        try:
            start_clock(work_time, count, "Work time!")
            count += 1
            completed( count )
            start_clock(rest_time, count, "Rest time!")
            play(bell)
            input("Press any key to begin the next pomodoro")
        except KeyboardInterrupt:
            savefile(count, date_time)
            break

if __name__ == "__main__":
    main()
