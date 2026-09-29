from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer('all-MiniLM-L6-v2')

with open("sample.txt") as file:
    text = file.read()

print(text)
print("Number of characters in the text:", len(text))

# Chunking
chunks = []

chunk_size = 25
chunk_overlap = 10
step = chunk_size - chunk_overlap

for i in range(0, len(text), step):
    chunk = text[i:i + chunk_size]
    chunks.append(chunk)

# print("Number of chunks created:", len(chunks))

# for i in range(len(chunks)):
#     print(f"Chunk {i}: {chunks[i]}")

# Embeddings
embeddings = model.encode(chunks)

print("Embeddings shape:", embeddings.shape)

# ChromaDB
client = chromadb.Client()

collection = client.create_collection(name="my_collection")

print("Collection created successfully.")

# IDs
ids = []

for i in range(len(chunks)):
    ids.append(str(i))

# Add to ChromaDB
collection.add(
    ids=ids,
    documents=chunks,
    embeddings=embeddings.tolist()
)

print("No of items in the collection:", collection.count())

# Get stored data
results = collection.get(ids=['5'])

for i in range(len(results['ids'])):
    print(
        f"ID: {results['ids'][i]} -> "
        f"Chunk: {results['documents'][i]}"
    )
chunk1 = collection.get(ids=['0'])
print(chunk1)