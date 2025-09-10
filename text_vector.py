import google.genai as genai

def embed_text(client, text):
    # テキストをベクトル化する関数（Google Gemini版）
    response = client.models.embed_content(
        model="models/text-embedding-004",  # Googleの埋め込みモデル
        contents=text
    )
    return response.embeddings[0].values 