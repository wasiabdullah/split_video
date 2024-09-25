from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
import os
from moviepy.editor import VideoFileClip


# Replace the filename below.
# required_video_file = "filename.mp4"
video_folder = 'video_folder'
with open("times.txt") as f:
  times = f.readlines()

times = [x.strip() for x in times] 
videos = sorted([f for f in os.listdir(video_folder) if f.endswith('.mp4')])


# with VideoFileClip(required_video_file) as video:
#     video_duration = video.duration
    

def get_video_duration(video_file):
        """
        Get the duration of the video file in seconds.
        
        :param video_file: Path to the video file.
        :return: Duration of the video in seconds.
        """
        # video_path = os.path.abspath(video_folder/video_file)
        with VideoFileClip(video_file) as video:
            return video.duration

os.chdir(video_folder)
for video in videos:
    
    vidname = video.split('.')[0]
    print(vidname)
    
    vidname =  video.split('.')[0]
    print(vidname)
    vid_dur = get_video_duration(video)
    print(vid_dur)
    
     
    
 
    for time in times:
        starttime = int(time.split("-")[0])
        endtime = int(time.split("-")[1])
        
        
        if starttime >= vid_dur:
            print(f"Start time {starttime} exceeds video duration ({vid_dur}). Skipping this clip.")
            continue

    # Adjust endtime if it exceeds the video duration
        if endtime > vid_dur:
            print(f"End time {endtime} exceeds video duration ({vid_dur}). Adjusting end time to {vid_dur}.")
            endtime = vid_dur
        
        ffmpeg_extract_subclip(video, starttime, endtime, targetname=vidname+str(times.index(time)+1)+".mp4")
