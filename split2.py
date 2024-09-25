from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os
from moviepy.editor import VideoFileClip

# Replace the filename below.
video_folder = 'video_folder'
 

videos = sorted([f for f in os.listdir(video_folder) if f.endswith('.mp4')])

def get_video_duration(video_file):
    """
    Get the duration of the video file in seconds.
    
    :param video_file: Path to the video file.
    :return: Duration of the video in seconds.
    """
    with VideoFileClip(video_file) as video:
        return video.duration

# Process all videos in the folder



os.chdir(video_folder)

for video in videos:
    vidname = video.split('.')[0]  # Video name without extension
    vid_dur = get_video_duration(video)
    print(f"Processing {vidname} with duration {vid_dur} seconds.")
    chunk_length = 0
    # take in put for chunk lenght from user for each video
    chunk_length = int(input(f"Enter chunk Length for {vidname} of duration {vid_dur} in seconds (only integers) : "))
    # Initialize start and end times
    starttime = 0
    part = 1  # To name each chunk as part1, part2, etc.
    
    # Divide video into chunks
    while starttime < vid_dur:
        endtime = starttime + chunk_length
        if endtime > vid_dur:
            endtime = vid_dur  # Last chunk will be the remaining length of the video
        
        # Define the output file name
        targetname = f"{vidname}_part_{part}.mp4"
        
        # Extract the subclip
        ffmpeg_extract_subclip(video, starttime, endtime, targetname=targetname)
        print(f"Created {targetname} from {starttime} to {endtime} seconds.")
        
        # Update starttime for the next chunk and increment the part number
        starttime = endtime
        part += 1
