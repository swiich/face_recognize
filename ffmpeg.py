import subprocess

ffmpegPath = "E:\Python\PycharmProjects\ImgHash\\ffmpeg-20170605-4705edb-win64-static\\bin\\ffplay.exe "
curMediaPath = "E:\Python\PycharmProjects\ImgHash\\img\\test.mp4"

cmd = ffmpegPath + curMediaPath
# os.popen(cmd)
# os.system(cmd)
subprocess.call(cmd)
