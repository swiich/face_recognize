import subprocess

ffmpegPath = 'D:\\ffmpeg-20170605-4705edb-win64-static\\bin\\ffmpeg.exe'
CurMediaPath = 'E:\Python\PycharmProjects\ImgHash\img\\test.mp4'
videoStartTime = '00:00:0.0'
videoEndTime = '00:01:0.0'
videoSaveDir = 'E:'


cmd = ffmpegPath + ' -y -i ' + CurMediaPath + ' -ss ' + videoStartTime + ' -t ' + videoEndTime +\
' -acodec copy -vcodec copy -async 1 ' + videoSaveDir

subprocess.call(cmd)