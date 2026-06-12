from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="gpt2"
)

result = generator(
    "Artificial Intelligence is",
    max_new_tokens=50,
    num_return_sequences=1
)

print(result[0]["generated_text"])