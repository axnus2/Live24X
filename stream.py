import subprocess

ffmpeg_process = None
current_hls_url = None

RTMP_URL = "rtmp://live.restream.io/live/re_7638211_event4c220a8725e842108313d235ea41e326"

def start_stream(input_url, output_hls="/tmp/live.m3u8"):
    global ffmpeg_process, current_hls_url
    if ffmpeg_process is None:
        current_hls_url = output_hls
        ffmpeg_process = subprocess.Popen([
            "ffmpeg",
            "-i", input_url,
            "-c:v", "copy",
            "-c:a", "aac",
            "-f", "tee",
            f"[f=hls]{output_hls}|[f=flv]{RTMP_URL}"
        ])
        print("Stream started")
    else:
        print("Stream already running")

def stop_stream():
    global ffmpeg_process, current_hls_url
    if ffmpeg_process:
        ffmpeg_process.terminate()
        ffmpeg_process = None
        current_hls_url = None
        print("Stream stopped")

def get_hls_url():
    return current_hls_url
