import acoustid
import os
import time
import csv
import re

def preprocess_text(text):
    text = re.sub(r"\(.*\)", "", text)
    text = re.sub(r"\[.*\]", "", text)
    text = re.sub(r"\{.*\}", "", text)
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
    text = re.sub(r"\s+", "", text)
    text = text.lower()
    text = re.sub("remix", "", text)
    text = re.sub("feat", "", text)
    text = re.sub("ft\.", "", text)
    text = re.sub("ft", "", text)
    return text

folder_paths = ["D:\\music\\rock", "D:\\music\\hiphop", "D:\\music\\jazz", "D:\\music\\folk", "D:\\music\\country", "D:\\music\\pop" , "D:\\music\\funk" , "D:\\music\\blues"]
# folder_paths = ["D:\\music\\rock"]
api_key = "b'bpfBSuie"

requests_per_second = 2
delay_between_requests = 1 / requests_per_second
no_matches = []
results= {}
count=0
api_error = []

for folder_path in folder_paths:
    items = os.listdir(folder_path)
    file_paths = [os.path.join(folder_path, item) for item in items if os.path.isfile(os.path.join(folder_path, item))]
    for file_path in file_paths:
        try:
            filename = os.path.basename(file_path)
            video_id , genre , title_file = filename.split("#")
            if str(video_id) in results:
                results[str(video_id)]["genres"].append(genre)
            else:
                matches = list(acoustid.match(api_key, file_path))
                formatted_file_title = preprocess_text(title_file)
                if not matches:
                    no_matches.append(file_path)
                else:
                    matches.sort(key=lambda x: x[0], reverse=True)
                    matched=False
                    recording_ids=[]
                    artist_name = None
                    title_name = None
                    for match in matches:
                        score, recording_id, title, artist = match
                        if (artist and preprocess_text(artist) in formatted_file_title) or (title and preprocess_text(title) in formatted_file_title):
                            if not matched:
                                artist_name = artist
                                title_name = title
                            matched=True
                            recording_ids.append(recording_id)
                    if not matched:
                        no_matches.append(file_path)
                    else:
                        results[str(video_id)] = {"file_name": filename, "recording_ids": recording_ids[:5] , "artist": artist_name , "title": title_name , "genres": [genre]}
                time.sleep(delay_between_requests)
                
        except Exception as e:
            print (e)
            api_error.append(file_path)
            time.sleep(delay_between_requests)
            continue
        
        finally:
            count+=1
            if count%25==0:
                print(count/2765)

print ("-"*90)
print (no_matches)
print (len(no_matches))
print ("-"*90)
print (api_error)
print (len(api_error))

with open('output3.csv', 'w', newline='',  encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=["video_id", "file_name", "recording_ids", "artist", "title", "genres"])
    writer.writeheader()
    for video_id, data in results.items():
        try:
            row = data.copy()
            row['video_id'] = video_id
            writer.writerow(row)
        except Exception as e:
            print (e)
            continue