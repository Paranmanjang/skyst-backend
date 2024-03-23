from pinecone import Pinecone, ServerlessSpec
from config import AI_Settings

pinecone_api_key = AI_Settings().pinecone_api_key

pc = Pinecone(api_key=pinecone_api_key)

# index = pc.create_index(
#   name="serverless-index",
#   dimension=3072,
#   metric="cosine",
#   spec=ServerlessSpec(
#     cloud="aws",
#     region="us-west-2"
#   )
# )

index = pc.Index("serverless-index")

def upload_vector(id: str, vector: list):
    index.upsert(vectors=[
        {"id": id, "values": vector}
        ]
    )

# top_k 개수만큼 가장 가까운 벡터를 찾아서 반환
def search_vector(vector: list, top_k: int):

    top_k_result = index.query(
        vector=vector,
        top_k=top_k,
        include_value=False
    )

    results = top_k_result['matches']

    print(results)

    ids = []
    for result in results:
        ids.append(int(result['id']))

    return ids