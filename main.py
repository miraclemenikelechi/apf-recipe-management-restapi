# Importing necessary modules
import starlette.status as status
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from routes.index import ingredients, recipes

# Creating the FastAPI server instance
server = FastAPI()

# Including routers for different parts of the application
server.include_router(recipes)
server.include_router(ingredients)


@server.get("/")
async def root():
    """
    Redirects incoming GET requests to the API documentation page.
    """

    # Redirecting to the API documentation page using a 302 status code
    return RedirectResponse(
        url="/docs",
        status_code=status.HTTP_302_FOUND,
    )


if __name__ == "__main__":
    # Importing uvicorn for running the FastAPI server
    import uvicorn

    # Configuration for the server's host and port
    HOST = "127.0.0.1"
    PORT = 8000

    # Running the FastAPI server with uvicorn
    uvicorn.run("main:server", host=HOST, port=PORT, reload=True)

