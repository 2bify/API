import models
from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from database import async_get_db

router=APIRouter(prefix="/search", tags=['Search DB'])
@router.get("/{video_id}")
async def search(video_id:str,db: AsyncSession = Depends(async_get_db)):
    video = await db.execute(select(models.Video).where(models.Video.video_id==video_id))
    return video.scalars().first()