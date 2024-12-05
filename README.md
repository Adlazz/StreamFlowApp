# StreamFlow Media Downloader 🎵

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamflow-media-downloader.streamlit.app/)

A powerful and user-friendly media downloader web application built with Streamlit that allows you to download content from various platforms in different formats and qualities.

## 🌟 Features

- **Multi-Platform Support**: Download content from various platforms including:
  - YouTube
  - Vimeo
  - SoundCloud
  - Dailymotion
  - Facebook Videos
  - Twitter Videos
  - And many more!

- **Format Options**:
  - Audio downloads (MP3, WAV)
  - Video downloads (MP4)
  - Customizable quality settings
  - Multiple resolution options (720p, 1080p, Best)
  - Audio quality options (192kbps, 256kbps, 320kbps)

- **Preview Features**:
  - Video information display
  - Thumbnail preview
  - Duration, views, and channel information
  - Real-time download progress

## 🚀 Live Demo

Try the application live at: [https://streamflow-media-downloader.streamlit.app/](https://streamflow-media-downloader.streamlit.app/)

## 🛠️ Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/streamflow-media-downloader.git
cd streamflow-media-downloader
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run streamlit_app.py
```

## 📋 Requirements

- Python 3.7+
- streamlit
- yt-dlp
- FFmpeg (for audio conversion)

Create a `requirements.txt` file with the following dependencies:
```
streamlit
yt-dlp
```

## 🎯 Usage

1. Visit the application URL or run it locally
2. Enter the URL of the media you want to download
3. Select your desired format (audio/video)
4. Choose the quality settings
5. Click "Get Information" to preview the content
6. Click "Download" to start the download process
7. Use the download button to save the file when ready

## ⚖️ Legal Disclaimer

This tool is provided for educational and personal use only. Users are responsible for ensuring all downloads comply with applicable laws and terms of service. The developers are not responsible for any misuse of this tool.

### Acceptable Uses
- Downloading your own content
- Content with explicit download permission
- Public domain material
- Content under Creative Commons licenses (following the specific license terms)

### Prohibited Uses
- Downloading copyrighted material without permission
- Commercial use of downloaded content without proper licenses
- Redistribution of downloaded content without authorization
- Downloading content that violates any applicable laws

## 🔒 Privacy

- No user data or download history is collected
- All downloads are temporary and deleted after completion
- The application does not store any downloaded content

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 💡 Technical Notes

- Uses yt-dlp for reliable media extraction
- Implements retry logic for robust downloads
- Includes proper error handling and user feedback
- Optimized for YouTube but works with multiple platforms
- Temporary file cleanup after downloads

## 🔧 Troubleshooting

If you encounter any issues:
1. Ensure your URL is valid and accessible
2. Check your internet connection
3. Verify that the content is available in your region
4. Make sure FFmpeg is properly installed for audio conversions

For additional help, please open an issue in the GitHub repository.
