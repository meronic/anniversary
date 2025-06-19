from fastapi import FastAPI, Request, Response, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()
app.add_middleware(SessionMiddleware, secret_key="change-me")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def get_index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/verify")
async def verify(request: Request):
    data = await request.json()
    if data.get("code") == "0425":
        request.session["unlocked"] = True
        return Response(status_code=status.HTTP_200_OK)
    return Response(status_code=status.HTTP_401_UNAUTHORIZED)


def check_unlocked(request: Request) -> bool:
    return request.session.get("unlocked") is True

@app.get("/letter", response_class=HTMLResponse)
async def letter(request: Request):
    if not check_unlocked(request):
        return RedirectResponse("/", status_code=302)
    return templates.TemplateResponse("letter.html", {"request": request})

@app.get("/photos", response_class=HTMLResponse)
async def photos(request: Request):
    if not check_unlocked(request):
        return RedirectResponse("/", status_code=302)
    return templates.TemplateResponse("photos.html", {"request": request})
