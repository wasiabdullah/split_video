import os
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip
import subprocess


# Download and install ffmpeg and add it to path variables in environment variables settings on windows

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

def ffmpeg_extract_subclip_custom(input_file, start_time, end_time, target_name):
    """
    Custom implementation of ffmpeg_extract_subclip to exclude non-video/audio streams.
    
    :param input_file: Path to the video file.
    :param start_time: Start time of the clip (in seconds).
    :param end_time: End time of the clip (in seconds).
    :param target_name: Name of the output file for the subclip.
    """
    cmd = [
        "ffmpeg",
        "-y",  # Overwrite output file if exists
        "-i", input_file,  # Input file
        "-ss", str(start_time),  # Start time
        "-to", str(end_time),  # End time
        "-c", "copy",  # Copy codec
        "-map", "0:v:0",  # Map only video stream
        "-map", "0:a:0?",  # Map only audio stream (if present)
        target_name  # Output file
    ]
    try:
        subprocess.run(cmd, check=True)
        print(f"Subclip saved as {target_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error processing {input_file}: {e}")

# chnge directory
os.chdir(video_folder)

for video in videos:
    vidname = video.split('.')[0]  # Video name without extension
    vid_dur = get_video_duration(video)
    print(f"Processing {vidname} with duration {vid_dur} seconds.")
    
    
    # you can hardcode the legth of chunk or take input from user for each file
    chunk_length = 400
    # take in put for chunk lenght from user for each video
    # chunk_length = int(input(f"Enter chunk Length for {vidname} of duration {vid_dur} in seconds (only integers) : "))
    
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
        
        # Extract the subclip using the custom function to exclude problematic streams
        ffmpeg_extract_subclip_custom(video, starttime, endtime, targetname)
        
        # Update starttime for the next chunk and increment the part number
        starttime = endtime
        part += 1
