import ollama

response = ollama.chat(

    model="llama3.2:3b",

    messages=[

        {

            "role": "user",

            "content": "Explain how AI is used in everyday life with 3 examples"

        }

    ]

)

print(response["message"]["content"])