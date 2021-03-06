![GafasDemo.jpg](http://i.dailymail.co.uk/i/pix/2012/07/25/article-2178792-14362C90000005DC-659_634x259.jpg)

_image designed by German Markus Gerke_

# InstagramPi

"Gafas" for Instagram with Raspberry Pi Zero

## Hardware

- Raspberry Pi Zero v1.3
- Camera Pi v1.3
- Cable Camera Pi

## Work

- Upload Video and photo Instagram
- Video Circular (Spectacles) [Example](https://www.instagram.com/p/BTFAyHPjp47/?taken-by=xhabas)
- Filters of PiCamera

## Instructions

1. Fork/Clone/Download this repo

    `git clone https://github.com/sabas1080/InstagramPi/`


2. Navigate to the directory

    `cd InstagramPi`


3. Install the dependencies

    `pip install -r requirements.txt`

4. Install ffmpeg for PiZero

```
  wget https://github.com/ccrisan/motioneye/wiki/precompiled/ffmpeg_3.1.1-1_armhf.deb
  dpkg -i ffmpeg_3.1.1-1_armhf.deb
```

5. Install ffmpeg for Pi2/Pi3/Mac/Linux/Windows (Link)[http://ffmpeg.org/download.html]

  ```
  git clone https://github.com/FFmpeg/FFmpeg.git

  cd FFmpeg

  sudo ./configure --arch=armel --target-os=linux --enable-gpl --enable-libx264 --enable-nonfree

  make

  sudo make install
  ```

6. Camera enabled.

Try running 'sudo raspi-config'

  `sudo raspi-config`

Interfacing Options->Camera->Enable - Yes

7. Reboot

8. Modify InstagramPi.py with your own username and password

9. Run the script (**use text editor to edit the script and type in valid Instagram username/password**)

  `python InstagramPi.py`


Andres Sabas @ Feb 2017


Contributing to this software is warmly welcomed. You can do this basically by<br>
[forking](https://help.github.com/articles/fork-a-repo), committing modifications and then [pulling requests](https://help.github.com/articles/using-pull-requests) (follow the links above<br>
for operating guide). Adding change log and your contact into file header is encouraged.<br>
Thanks for your contribution.

Enjoy!
