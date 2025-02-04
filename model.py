# Use a pipeline as a high-level helper
from transformers import pipeline

translator = pipeline("translation", model="PaulineSanchez/autotrain-translation_food_english_to_french-52830124391")

