import os
def merge_youtube_urls(file_paths):
    # Create a set to store unique URLs
    unique_urls = set()

    # Open the output file in append mode
    with open('merged_urls_3.txt', 'a') as output_file:
        for file_path in file_paths:
            # Open the input file
            with open(file_path, 'r') as input_file:
                # Read each line from the input file
                for line in input_file:
                    # Extract the YouTube URL from the line
                    url = line.strip()

                    # Check if the URL is unique
                    if url not in unique_urls:
                        # Add the unique URL to the set and write it to the output file
                        unique_urls.add(url)
                        output_file.write(url + '\n')
        print (len(unique_urls))

# Example usage
# file_paths = ["C:\\Users\\harsh\\Desktop\\playlists\\blues-playlist-1", "C:\\Users\\harsh\\Desktop\\playlists\\country-playlist-1", "C:\\Users\\harsh\\Desktop\\playlists\\folk-playlist-1", "C:\\Users\\harsh\\Desktop\\playlists\\funk-playlist-1", "C:\\Users\\harsh\\Desktop\\playlists\\jazz-playlist-1"]
file_paths = ["D:\\workspace\\MLProject\\merge-all-1.txt","D:\\workspace\\MLProject\\merged_urls_2.txt" ]
merge_youtube_urls(file_paths)