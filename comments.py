from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from config import settings
# Replace the API key with your own.
api_key = settings.youtube_api_key
youtube = build('youtube', 'v3', developerKey=api_key)
# Search for videos with the query "python tutorial".
async def get_comments(video_id):
    comments = []
    
    try:
        video_response = youtube.videos().list(
        part='statistics',
        id=video_id
        ).execute()

        # Check if comments are enabled
        comment_count = video_response.get("items")[0].get("statistics").get("commentCount")
        print("comment count", comment_count)
        # Fetch comments if enabled
        if comment_count != "0" and comment_count != None:
            print("Entered block")
            comments_response = youtube.commentThreads().list(
                    part='snippet',
                    videoId=video_id,
                    textFormat='plainText',
                    maxResults=100,
                ).execute()
            # iterate video response
            c=0
            while comments_response:
                c+=1
                if(c>200):
                    break
                else:
                    for item in comments_response['items']:
                        comment = item['snippet']['topLevelComment']['snippet']['textDisplay']
                        comments.append(comment)    
                    if 'nextPageToken' in comments_response:
                        comments_response = youtube.commentThreads().list(
                                part = 'snippet',
                                videoId = video_id,
                                textFormat='plainText',
                                maxResults=100,
                                pageToken=comments_response['nextPageToken']
                            ).execute()
                    else:
                        break
            return comments
        else:
            return comments
    except HttpError as e:
        print(f'An error occurred while fetching comments: {e}')
        return comments
