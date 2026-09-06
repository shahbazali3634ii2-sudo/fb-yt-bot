import os
import yt_dlp
import subprocess

def process_video_for_platforms(video_url, target_platform="instagram"):
    print(f"📥 Downloading source video for target platform: {target_platform}...")
    
    ydl_opts = {
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=mp4]/best[ext=mp4]',
        'outtmpl': 'source_video.mp4',
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
    print("✅ Video downloaded successfully!")

    # Platform-specific duration limits
    # Instagram Reels: up to 90 seconds
    # YouTube Shorts & TikTok: up to 60 seconds (1-minute parts)
    
    segment_time = 60  # Default for YouTube Shorts & TikTok
    if target_platform.lower() == "instagram":
        segment_time = 90  # Instagram limit adjustment
    elif target_platform.lower() == "facebook":
        segment_time = 60  # Facebook Reels limit

    print(f"✂️ Processing and cutting video into {segment_time}-second segments for {target_platform}...")
    subprocess.run([
        'ffmpeg', '-i', 'source_video.mp4', 
        '-c:v', 'libx264', '-crf', '23', 
        '-preset', 'fast', '-c:a', 'aac', 
        '-f', 'segment', '-segment_time', str(segment_time), 
        '-reset_timestamps', '1', 
        f'output_{target_platform}_part_%03d.mp4'
    ])
    print(f"✅ Video successfully optimized and split for {target_platform}!")

    # Platform auto-upload integration point
    print(f"🚀 Ready to auto-upload parts to {target_platform} API...")

if __name__ == "__main__":
    # Aap yahan platform ka naam aur video link set kar sakte hain
    platform = os.getenv("TARGET_PLATFORM", "instagram") # options: instagram, tiktok, youtube, facebook
    link = os.getenv("TARGET_URL", "YOUR_VIDEO_LINK_HERE")
    
    if "YOUR_VIDEO" not in link:
        process_video_for_platforms(link, platform)
    else:
        print("⚠️ Please provide a valid video link.")
  
