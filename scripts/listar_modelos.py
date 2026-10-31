import json, os, urllib.request
from dotenv import load_dotenv

load_dotenv()
req = urllib.request.Request(
    "https://generativelanguage.googleapis.com/v1beta/models?pageSize=100",
    headers={"x-goog-api-key": os.environ["GEMINI_API_KEY"]})
data = json.loads(urllib.request.urlopen(req, timeout=60).read())
for m in data["models"]:
    if "generateContent" in m.get("supportedGenerationMethods", []):
        print(m["name"].replace("models/", ""))