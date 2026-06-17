from youtube_transcript_api import YouTubeTranscriptApi

api = YouTubeTranscriptApi()
video_id = "Mp8m-ysmfq4"
video_name = "justin-welsh-seven-figure-business"

transcript = api.fetch(video_id)

text = " ".join([item.text for item in transcript])

with open(
    f"research/youtube-transcripts/{video_name}.md",
    "w",
    encoding="utf-8"
) as f:
    f.write(f"# {video_name}\n\n")
    f.write(f"Video ID: {video_id}\n\n")
    f.write(text)

print("Saved!")