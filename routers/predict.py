from fastapi import APIRouter
import comments
import prediction

from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from config import settings

api_key = settings.youtube_api_key
youtube = build('youtube', 'v3', developerKey=api_key)

router=APIRouter(prefix="/predict", tags=['prediction'])
@router.get("/{video_id}")
async def predict(video_id:str):
    comment_data=await comments.get_comments(video_id)
    predict_array=[]
    if(len(comment_data)>30):
        predict_array = await prediction.load_predict(comment_data)
        predict_array = list(predict_array)
        percent = predict_array.count(4)/len(predict_array)*100
        percent = round(percent)
        return {"video_id":video_id,
            "predicted_score":percent,
            "no_of_comments":len(predict_array),
            "p_comments":predict_array.count(4)}
    elif(len(comment_data)<=30 and len(comment_data)>=5):
        video_response = youtube.videos().list(
        part='statistics',
        id=video_id
        ).execute()
        view_count = video_response.get("items")[0].get("statistics").get("viewCount")
        like_count = video_response.get("items")[0].get("statistics").get("likeCount")
        if(view_count==None):
            view_count=0
        if(like_count==None):
            like_count=0
        predict_array = await prediction.load_predict(comment_data)
        predict_array = list(predict_array)
        print(f"predict array of video_id={video_id}: ",len(predict_array))
        percent = predict_array.count(4)/len(predict_array)*100
        if(view_count!=0):
            percent = (float(like_count)//float(view_count)) * 50 + (percent * 0.5)
        percent = round(percent)
        return {"video_id":video_id,
            "predicted_score": percent,
            "no_of_comments":len(predict_array),
            "p_comments":predict_array.count(4)}
    else:
        return {"video_id":video_id,
            "predicted_score": -1,
            "no_of_comments":0,
            "p_comments":0}