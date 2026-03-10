import asyncio
from concurrent.futures import ThreadPoolExecutor
from typing import NewType, TypeAlias

from sqlalchemy.ext.asyncio import AsyncSession

MainAsyncSession: TypeAlias = AsyncSession
HasherThreadPoolExecutor = NewType("HasherThreadPoolExecutor", ThreadPoolExecutor)
HasherSemaphore = NewType("HasherSemaphore", asyncio.Semaphore)
