from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import settings

SQLALCHEMY_DATABASE_URL = f"postgresql+asyncpg://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"
engine = create_async_engine(SQLALCHEMY_DATABASE_URL, future=True, echo=True)
#SessionLocal=sessionmaker(autocommit=False, autoflush=False, bind=engine)


async_session = sessionmaker(bind=engine, expire_on_commit=False, class_=AsyncSession)

Base=declarative_base()

async def async_get_db() -> AsyncSession:
    async with async_session() as session:
        try:
            yield session
        finally:
            session.close()