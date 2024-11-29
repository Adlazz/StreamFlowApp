import streamlit as st
import yt_dlp
import os
from datetime import datetime
import subprocess

def setup_download_dir():
    """Create temporary directory for downloads"""
    if not os.path.exists("downloads"):
        os.makedirs("downloads")
    return "downloads"

def get_video_info(url):
    """Get video information without downloading"""
    ydl_opts = {
        'quiet': True,
        'no_warnings': True,
        'extract_flat': True,
        'nocheckcertificate': True,
        'ignoreerrors': False,
        # Add user agent
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        # Add referer
        'referer': 'https://www.youtube.com/'
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            return info
    except Exception as e:
        st.error(f"Error getting video info: {str(e)}")
        return None

def download_content(url, format_type, quality, audio_format="mp3"):
    """Download content with specified options"""
    download_dir = setup_download_dir()
    
    # Base options with additional parameters
    ydl_opts = {
        'outtmpl': os.path.join(download_dir, '%(title)s.%(ext)s'),
        'quiet': False,
        'no_warnings': False,
        'nocheckcertificate': True,
        'ignoreerrors': False,
        'geo_bypass': True,
        'user_agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'referer': 'https://www.youtube.com/',
        'format_sort': ['res','ext'],
        'extractor_retries': 5,
        'file_access_retries': 5,
        'fragment_retries': 5,
        'retries': 5
    }
    
    try:
        if format_type == "audio":
            ydl_opts.update({
                'format': 'bestaudio',  # Changed from bestaudio/best
                'extractaudio': True,
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': audio_format,
                    'preferredquality': quality,
                }],
            })
        else:
            if quality == "best":
                format_spec = 'bestvideo+bestaudio/best'
            else:
                format_spec = f'bestvideo[height<={quality}]+bestaudio/best[height<={quality}]'
            
            ydl_opts.update({
                'format': format_spec,
                'merge_output_format': 'mp4'
            })
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            try:
                # Primero intentamos obtener la info
                info = ydl.extract_info(url, download=False)
                if info is None:
                    raise Exception("No se pudo obtener la información del video")
                
                # Si la info está bien, procedemos con la descarga
                info = ydl.extract_info(url, download=True)
                if format_type == "audio":
                    return os.path.join(download_dir, f"{info['title']}.{audio_format}")
                else:
                    return os.path.join(download_dir, f"{info['title']}.mp4")
                    
            except yt_dlp.utils.DownloadError as e:
                st.error(f"Error de descarga: {str(e)}")
                return None
                
    except Exception as e:
        st.error(f"Error durante la descarga: {str(e)}")
        if hasattr(e, 'msg'):
            st.error(f"Detalles adicionales: {e.msg}")
        return None

def main():
    st.set_page_config(page_title="Media Downloader", page_icon="🎵")
   
    st.title("🎵 Media Downloader")
    st.write("Download your favorite content in various formats")
    
    # Nueva sección de información
    with st.expander("ℹ️ Supported Platforms & Usage Guidelines"):
        st.markdown("""
        ### 📥 Supported Platforms
        This downloader works with many popular platforms, including:
        - YouTube
        - Vimeo
        - SoundCloud
        - Dailymotion
        - Facebook Videos
        - Twitter Videos
        - And many more!
        
        ### ⚖️ Legal & Copyright Information
        **Important Legal Disclaimer:**
        
        This tool is provided for legitimate and legal use only. Before downloading any content, please ensure:
        
        1. You have the right to download and use the content
        2. The download complies with the platform's terms of service
        3. You respect intellectual property rights and copyright laws
        4. You have permission from the content creator when required
        
        ### 🚫 Prohibited Uses
        - Downloading copyrighted material without permission
        - Commercial use of downloaded content without proper licenses
        - Redistribution of downloaded content without authorization
        - Downloading content that violates any applicable laws
        
        ### ✅ Acceptable Uses
        - Downloading your own content
        - Content with explicit download permission
        - Public domain material
        - Content under Creative Commons licenses (following the specific license terms)
        
        ### 🔒 Privacy & Data Usage
        - This tool does not store any downloaded content
        - All downloads are temporary and deleted after completion
        - No user data or download history is collected
        
        By using this tool, you acknowledge that you have read and agree to these terms and will use the service responsibly.
        """)
    
    # Disclaimer existente actualizado
    st.warning("""
    ⚠️ DISCLAIMER: This tool is for educational and personal use only. 
    Users are responsible for ensuring all downloads comply with applicable laws and terms of service.
    Respect copyright laws and content creators' rights.
    The developers of this tool are not responsible for misuse.
    """)
    
    # Input fields
    url = st.text_input("Enter URL:")
    format_type = st.selectbox("Select Format:", ["audio", "video"])
    
    # Quality options based on format type
    if format_type == "audio":
        audio_format = st.selectbox("Select Audio Format:", ["mp3", "wav"])
        quality = st.selectbox("Select Quality:", ["192", "256", "320"])
        quality_text = f"{quality}kbps"
    else:
        quality = st.selectbox("Select Quality:", ["720", "1080", "best"])
        quality_text = "Best Quality" if quality == "best" else f"{quality}p"
    
    if st.button("Get Information"):
        if url:
            with st.spinner("Fetching video information..."):
                info = get_video_info(url)
                if info:
                    st.write("---")
                    st.write("📺 **Video Information**")
                    st.write(f"**Title:** {info.get('title', 'N/A')}")
                    st.write(f"**Channel:** {info.get('channel', 'N/A')}")
                    st.write(f"**Duration:** {info.get('duration_string', 'N/A')}")
                    st.write(f"**Views:** {info.get('view_count', 'N/A'):,}")
                    
                    # Show thumbnail
                    if 'thumbnail' in info:
                        st.image(info['thumbnail'], use_container_width=True)
    
    if st.button("Download"):
        if url:
            with st.spinner(f"Downloading {format_type} in {quality_text}..."):
                output_file = download_content(
                    url, 
                    format_type, 
                    quality, 
                    audio_format if format_type == "audio" else "mp4"
                )
                
                if output_file and os.path.exists(output_file):
                    with open(output_file, 'rb') as file:
                        mime_type = "audio/wav" if format_type == "audio" and audio_format == "wav" else "audio/mp3" if format_type == "audio" else "video/mp4"
                        st.download_button(
                            label="Download File",
                            data=file,
                            file_name=os.path.basename(output_file),
                            mime=mime_type
                        )
                    # Clean up
                    os.remove(output_file)
                else:
                    st.error("Download failed. Please try again.")

if __name__ == "__main__":
    main()