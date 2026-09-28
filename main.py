import os
import uvicorn
import contextlib
from fastapi import FastAPI

from server import mcp

# @contextlib.asynccontextmanager
# async def lifespan(app: FastAPI):
#     async with contextlib.AsyncExitStack() as stack:
#         await stack.enter_async_context(mcp.session_manager.run())
#         yield

mcp_app = mcp.http_app()

app = FastAPI(title = 'Expense Tracker', lifespan= mcp_app.lifespan)

app.mount("/expense", mcp_app)

port = int(os.environ.get("PORT", 10000))

if __name__=='__main__':
    uvicorn.run(app = app, host = '0.0.0.0', port = port)