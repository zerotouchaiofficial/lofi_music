import pickle
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

VIDEO_FILE = "final_video.mp4"

def upload_video():
    with open("token.pickle", "rb") as token:
        creds = pickle.load(token)

    youtube = build("youtube", "v3", credentials=creds)

    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": "Lofi Chill Beats 🎧 | Zero Touch AI",
                "description": "Auto generated lofi music\n\n#lofi #study #chill",
                "tags": ["lofi", "chill", "beats"],
                "categoryId": "10"
            },
            "status": {
                "privacyStatus": "public"
            }
        },
        media_body=MediaFileUpload(VIDEO_FILE, resumable=True)
    )

    response = request.execute()
    print("✅ Uploaded Video ID:", response["id"])

if __name__ == "__main__":
    upload_video()
