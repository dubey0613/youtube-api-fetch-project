# models/video.py
from sqlalchemy import Column, String, Text, TIMESTAMP
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func

Base = declarative_base()

class Video(Base):
    __tablename__ = 'youtube_data'
    
    video_id = Column(String(255), primary_key=True, nullable=False)
    title = Column(Text, nullable=False)
    description = Column(Text, nullable=True)
    published_at = Column(TIMESTAMP, nullable=False)
    thumbnails = Column(Text, nullable=True)
    created_at = Column(TIMESTAMP, default=func.now(), nullable=False)

    def __repr__(self):
        return f"<Video(video_id={self.video_id}, title={self.title})>"
