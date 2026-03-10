from fastapi import FastAPI
from app.twitch.oauth import router as twitch_oauth_router
from app.twitch.eventsub import router as twitch_eventsub_router

app = FastAPI(title="Twitch Music Points")

app.include_router(twitch_oauth_router, prefix="/auth/twitch", tags=["twitch-auth"])
app.include_router(twitch_eventsub_router, prefix="/webhooks/twitch", tags=["twitch-webhooks"])

@app.get("/health")
def health():
    return {"ok": True}
