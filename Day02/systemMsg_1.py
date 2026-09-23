import ollama
response = ollama.chat(
messages = [
    {
        "role": "system",
        "content": "Give answers in 2 lines only"
    },
    {
        "role": "user",
        "content": "Explain AI"
    }
  ]
)
print(response["message"]["content"])