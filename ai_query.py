import ollama
response = ollama.chat(
    mode1="llama3.2:3b";
    messages=[
        {
            "role:"user",
            "content":"Explain learning in 40 words"
        }
    ]
)
print(response["message"]["content"])