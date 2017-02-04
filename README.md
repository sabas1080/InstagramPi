# InstagramPi
"Gafas" for Instagram with Raspberry Pi Zero

##Hardware
- Raspberry Pi Zero 1.3
- Camera Pi 1.3
- Cable Camera Pi

`pip install -r requirements.txtinstall
`

```
wget http://ffmpeg.org/releases/ffmpeg-3.2.2.tar.bz2

tar xvjf ffmpeg-3.2.2.tar.bz2

cd ffmpeg-3.2.2

./configure --enable-gpl --enable-postproc --enable-swscale --enable-avfilter --enable-libmp3lame --enable-libvorbis --enable-libtheora --enable-libx264 --enable-libspeex --enable-shared --enable-pthreads --enable-libopenjpeg --enable-libfaac --enable-nonfree

make

sudo make install
```

##TODO
- Video Circular
- Filters
