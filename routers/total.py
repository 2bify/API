from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from database import async_get_db
from models import Video

router = APIRouter(prefix="/total", tags=["Total"])

@router.get("/")
async def get_total(db: AsyncSession = Depends(async_get_db)):
    query = select(Video)
    result = await db.execute(query)
    total_no_of_comments = sum([video.no_of_comments for video in result.scalars()])
    result = await db.execute(query)
    total_p_comments = sum([video.p_comments for video in result.scalars()])
    return {"total_no_of_comments": total_no_of_comments, "total_p_comments": total_p_comments}