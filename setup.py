from sentence_transformers import SentenceTransformer, util
from datasets import load_dataset

ds = load_dataset("Scuccorese/food-ingredients-dataset", split="train")
model = SentenceTransformer('sentence-transformers/all-MiniLM-L12-v2')
