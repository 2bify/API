import models , schemas
from fastapi import status, HTTPException,Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from database import async_get_db
from sqlalchemy.future import select

router=APIRouter(prefix="/add_data", tags=['Add to DB'])
@router.post("/", status_code=status.HTTP_201_CREATED)
async def add_data(video:schemas.Video_Output,db: AsyncSession = Depends(async_get_db)):
    search_video = await db.execute(select(models.Video).where(models.Video.video_id==video.video_id))
    if not search_video.scalars().first():
        new_video = models.Video(**video.dict())
        db.add(new_video)
        await db.commit()
        await db.refresh(new_video)
    else:
        raise HTTPException(status_code=status.HTTP_502_BAD_GATEWAY, detail=f'video with id: {video.video_id} is already in database')
    return new_video