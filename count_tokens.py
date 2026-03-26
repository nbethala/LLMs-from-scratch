import importlib
import importlib.metadata
import tiktoken

print("tiktoken version:", importlib.metadata.version("tiktoken"))

tokenizer = tiktoken.get_encoding("gpt2")

with open("the-verdict.txt", "r", encoding="utf-8") as f:
    raw_text =f.read()

enc_text = tokenizer.encode(raw_text)
print("Number of tokens:", len(enc_text))

