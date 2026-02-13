import os
import pickle
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]

def authenticate():
    creds = None
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    if not creds:
        flow = InstalledAppFlow.from_client_secrets_file(
            "client_secret.json", SCOPES
        )
        creds = flow.run_console()
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    return build("youtube", "v3", credentials=creds)


def upload():
    youtube = authenticate()

    with open("meta.txt", "r") as f:
        content = f.read().split("---")
        title = content[0].strip()
        description = content[1].strip()

    request_body = {
        "snippet": {
            "title": title,
            "description": description,
            "categoryId": "10"
        },
        "status": {
            "privacyStatus": "public"
        }
    }

    media = MediaFileUpload("final_video.mp4", resumable=True)

    response = youtube.videos().insert(
        part="snippet,status",
        body=request_body,
        media_body=media
    ).execute()

    video_id = response["id"]

    youtube.thumbnails().set(
        videoId=video_id,
        media_body=MediaFileUpload("thumbnail.jpg")
    ).execute()

    print("Uploaded:", video_id)


if __name__ == "__main__":
    upload()
