from yt_dlp import YoutubeDL
from youtube_transcript_api import YouTubeTranscriptApi
import os
import re

experts = [
    "Justin Welsh",
    "Guillaume Moubeche",
    "Ross Simmonds"
]

os.makedirs("research/youtube-transcripts", exist_ok=True)

api = YouTubeTranscriptApi()

ydl_opts = {
    "quiet": True,
    "extract_flat": True,
    "skip_download": True,
}

for expert in experts:
    print(f"\nSearching videos for {expert}...")

    try:
        with YoutubeDL(ydl_opts) as ydl:
            results = ydl.extract_info(
                f"ytsearch3:{expert}",
                download=False
            )

        for video in results["entries"]:
            try:
                video_id = video["id"]
                title = video["title"]

                safe_name = re.sub(r'[^a-zA-Z0-9_-]', '_', title)[:80]

                print(f"  Downloading transcript: {title}")

                transcript = api.fetch(video_id)

                text = " ".join([item.text for item in transcript])

                filename = (
                    f"research/youtube-transcripts/"
                    f"{expert.replace(' ', '-').lower()}_{safe_name}.md"
                )

                with open(filename, "w", encoding="utf-8") as f:
                    f.write(f"# {title}\n\n")
                    f.write(f"Expert: {expert}\n\n")
                    f.write(f"Video ID: {video_id}\n\n")
                    f.write(
                        f"URL: https://www.youtube.com/watch?v={video_id}\n\n"
                    )
                    f.write("## Transcript\n\n")
                    f.write(text)

                print(f"    Saved!")

            except Exception as e:
                print(f"    Failed transcript: {e}")

    except Exception as e:
        print(f"Failed expert {expert}: {e}")

print("\nDone!")