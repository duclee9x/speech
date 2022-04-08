import sounddevice as sd
from scipy.io.wavfile import write
import pandas as pd
import time
import os
from unidecode import unidecode

fs = 16000   # Sample rate (đề bài 16khz)
number_of_channel = 1 # ghi âm với 1 channel
seconds = 2  # Giây ghi âm

my_name = unidecode("Lê Đăng Đức") # Thay đổi cái này phù hợp với cá nhân 
my_ID = 51703059                   # Thay đổi cái này phù hợp với cá nhân 
number_of_each_file = 10            # Thay đổi cho phù hợp về đề bài (đề bài mỗi tên ghi 10 files)

a = pd.read_csv('student_list.csv')
a['full_name'] = a['last_name'].str.strip() + ' ' + a['first_name'].str.strip()

def wait_for_next_record(seconds, txt):
    for i in range(seconds):
        print(f"Đọc `{txt}` trong {seconds-i} giây nữa")
        time.sleep(1)
    os.system('clear')
    print(f"ĐỌC {txt}")


current_path = os.path.join(os.path.abspath(os.getcwd()), 'audio')
if not os.path.exists(current_path):
    os.makedirs(current_path)

for i in range(len(a)):
    for j in range(number_of_each_file):
        speaker_name = a['full_name'][i]
        file_name = f"{my_name.replace(' ','')}_{unidecode(speaker_name.replace(' ',''))}_{j}.wav"
        file_path = os.path.join(current_path,file_name)

        if os.path.exists(file_path):
            continue
        wait_for_next_record(3, speaker_name)
        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=number_of_channel)
        sd.wait()  # Wait until recording is finished
        write(file_path, fs, myrecording)  # Save as WAV file
        print(f"Xong, đã lưu: {file_name}")
