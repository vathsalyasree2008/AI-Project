import ollama
response=ollama.chat(
    model="llama3.2:3b",
    messages=[
        {
            "role":"user",
            "content":"""
1.Cat --  Animal
2.Rose -- Plant
3.Dog -- Animal
4.Mango -- ?
"""   }
    ]
)
print(response["message"]["content"])