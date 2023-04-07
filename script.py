import models , schemas
from sqlalchemy.ext.asyncio import AsyncSession
from database import async_get_db
from datetime import datetime, timedelta
from sqlalchemy import delete, and_
db = async_get_db()

now = datetime.utcnow()

# Calculate the cutoff time 30 days ago
check_time = now - timedelta(days=30)

db.execute(delete(models.Video).where(and_(models.Video.created_at < check_time)))
db.commit()
db.refresh(models.Video)