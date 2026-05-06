from pathlib import Path
import os

# Project root = 2 levels up from this file
ROOT_DIR = Path(__file__).resolve().parents[2]

# Allow override via env var
DATA_DIR = Path(os.getenv("DATA_DIR", ROOT_DIR / "assignment_2" / "data"))

RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"

TRAIN_FILE = RAW_DATA_DIR / "training_set_VU_DM.csv"
TEST_FILE = RAW_DATA_DIR / "test_set_VU_DM.csv"