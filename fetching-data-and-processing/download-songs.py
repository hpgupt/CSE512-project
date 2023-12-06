import os
import subprocess

url_file = "c:\\Users\\harsh\\Desktop\\playlists\\country-playlist-1.txt"
output_directory = "D:\\music\\country"
genre="country"
s = set()
c=0
with open(url_file, 'r') as file:
    for url in file:
        try:
            url = url.strip()
            video_id = url.split('=')[-1]
            if url and video_id not in s:
                s.add(video_id)
                output_template = os.path.join(output_directory, f"{video_id}#{genre}#%(title)s.%(ext)s")
                subprocess.run(f"yt-dlp -f bestaudio -o \"{output_template}\" {url}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        
        except Exception as e:
            print(f"Error downloading {url}: {e}")
            continue
        
        finally:
            c+=1
            print (f"Dowloaded {c} songs")

print("Download complete.")
