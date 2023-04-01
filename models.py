from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from database import Base
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

class Video(Base):
    __tablename__ = "video_data"
    video_id = Column(String, primary_key=True, nullable=False)
    predicted_score = Column(Integer,nullable=False)
    no_of_comments = Column(Integer,nullable=False)
    p_comments = Column(Integer,nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), server_default=text('now()'), nullable=False)