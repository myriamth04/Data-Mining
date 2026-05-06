import polars as pl
from .config import TRAIN_FILE, TEST_FILE

def load_train():
    return pl.read_csv(TRAIN_FILE)

def load_test():
    return pl.read_csv(TEST_FILE)