import uvicorn
from pathlib import Path

if __name__ == "__main__":
    uvicorn.run("src.presentation.server:app", host='0.0.0.0', port=7200, log_level="info", reload=True, workers=2)