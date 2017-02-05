# InstagramPi
"Gafas" for Instagram with Raspberry Pi Zero

##Hardware
- Raspberry Pi Zero v1.3
- Camera Pi v1.3
- Cable Camera Pi

1. Fork/Clone/Download this repo

    `git clone https://github.com/sabas1080/InstagramPi/`


2. Navigate to the directory

    `cd InstagramPi`


3. Install the dependencies

    `pip install -r requirements.txt`

4. Install ffmpeg

```
git clone https://github.com/FFmpeg/FFmpeg.git

cd FFmpeg

sudo ./configure --arch=armel --target-os=linux --enable-gpl --enable-libx264 --enable-nonfree

make

sudo make install
```

5. Camera enabled. Try running 'sudo raspi-config'

`sudo raspi-config`
Interfacing Options->Camera->Enable - Yes

6. Reboot

7. Modify InstagramPi.py with your own username and password

8. Run the script (**use text editor to edit the script and type in valid Instagram username/password**)

  `python InstagramPi.py`


##TODO

- Video
- Video Circular
- Filters

Andres Sabas @ Feb 2017
