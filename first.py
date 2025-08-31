import streamlit as st
import yt_dlp
import os

def downloadVideo(url):
    ydl_opts = {
        'format': 'best',
        'outtmpl': 'downloads/%(title)s.%(ext)s'  # Save in "downloads" folder
    }

    with st.spinner("Downloading... Please wait."):
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            file_path = ydl.prepare_filename(info)
    return file_path

st.title("🎬 DevilNetworking - YouTube Downloader")

# Input
video_link = st.text_input("Enter Video URL", placeholder="Paste YouTube link here")

# Button
if st.button("Download"):
    if video_link.strip():
        try:
            file_path = downloadVideo(video_link)
            st.success(f"✅ Video Downloaded Successfully!")
            st.write(f"Saved at: `{os.path.abspath(file_path)}`")
        except Exception as e:
            st.error(f"❌ Error: {e}")
    else:
        st.warning("⚠️ Please enter a valid URL")
