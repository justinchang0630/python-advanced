from pytube import YouTube


def get_movie():
    get_url = url_info.get()
    get_name = name_info.get() + ".mp4"
    yt = Youtube(get_url)
    print("we are downloading videos")
    video = yt.streams
    result = video.filter(progressive=True, subtype="mp4", res="360p")
    print(result)
    dest = "20211128"
    load_name = get_name
    result[0].download(progressive=True, subtype="mp4", res="360p")
    print(result[0])
    print("Download Finished")
    movie_name.config(text="電影名稱:" + get_name)
    movie_time.config(text="電影時間:" + str(yt.length) + "sec")


# windows = Tk()
# windows.title("下載影片")

# Youtube("https://www.youtube.com/")
yt = YouTube("https://youtu.be/1iXJDHDmEdk")
print("we are downloading videos")

video = yt.streams
length = len(video)
for i in range(length):
    print(video[i])
print("影片名稱:", yt.title)
print("影片作者:", yt.author)
print("影片長度:", yt.length, "秒")
print("縮圖網址:", yt.thumbnail_url)

result[0].download(output_path=dest, filename=fname)

clip = VideoFileClip(dest + fname)
clip.preview()
