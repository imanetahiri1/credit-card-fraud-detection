import sys
from pathlib import Path


V4_PATH = Path(__file__).resolve().parents[1]

if str(V4_PATH) not in sys.path:
    sys.path.insert(0, str(V4_PATH))