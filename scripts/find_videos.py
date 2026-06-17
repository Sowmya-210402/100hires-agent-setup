from yt_dlp import YoutubeDL

search_query = "Justin Welsh"

ydl_opts = {
    "quiet": True,
    "extract_flat": True,
    "skip_download": True,
}

with YoutubeDL(ydl_opts) as ydl:
    results = ydl.extract_info(
        f"ytsearch10:{search_query}",
        download=False
    )

print(f"\nFound {len(results['entries'])} videos:\n")

for i, video in enumerate(results["entries"], start=1):
    print(f"{i}. {video['title']}")
    print(f"   Video ID: {video['id']}")
    print(f"   URL: https://www.youtube.com/watch?v={video['id']}")
    print()