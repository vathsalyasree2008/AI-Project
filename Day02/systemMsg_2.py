import ollama

response = ollama.chat(

    model="llama3.2:3b",

    messages=[

        {
            "role": "system",
            "content": "Give answers in very simple language so that a 5-year-old can understand"
        },

        {
            "role": "user",
            "content": "Explain AI"
        }

    ]

)

print(response["message"]["content"])