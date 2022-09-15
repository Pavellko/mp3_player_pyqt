    ######
    # video = pafy.new(link_youtube)
    # bestaudio = video.getbestaudio()
    # bestaudio.download(f'{video.title}.mp3')
    ######
    # ydl_opts = { 'format': 'm4a/bestaudio/best', 'postprocessors': [{  'key': 'FFmpegExtractAudio', 'preferredcodec': 'mp3', }]}
    # with YoutubeDL() as ydl:
    #     ydl.download([link_youtube])
    #######
    # yt_download(link_youtube, f'{video.title}.mp3' , ismusic=True, codec = "mp3")
    #######
    # video_info = YoutubeDL().extract_info( url = link_youtube, download=False )
    # filename = f"{video_info['title']}.mp3"
    # options={
    #     'format':'bestaudio/best',
    #     'keepvideo':False,
    #     'outtmpl':filename,
    #      }

    # with YoutubeDL(options) as ydl:
    #     ydl.download([video_info['webpage_url']])
    ########