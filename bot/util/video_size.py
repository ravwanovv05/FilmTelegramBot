import os
from bot.dispatcher import bot


async def get_video_size(video_path):
    await bot.get_file()
    size_in_bytes = os.path.getsize(video_path)
    size_in_mb = size_in_bytes / (1024 * 1024)

    return size_in_mb


# Misol qo'llash
video_path = "/home/kali/Videos/oQKWZynNh89wAfXHKQkIzogDqSCaAPzNCEYNIO.mp4"
size_in_mb = get_video_size(video_path)
print(f"Video hajmi: {size_in_mb:.2f} MB")
