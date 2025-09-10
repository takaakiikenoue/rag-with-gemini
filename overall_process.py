from gemini_API import client
from web_scraping import get_webpage_text
from text_division import split_into_chunks
from text_vector import embed_text
from text_Similarity_calculation import find_relevant_chunks
from answer_Generate import generate_answer


def rag_qa(url, question):
    """RAGを使った質問応答システムのメイン関数"""

    # 1. Webページからテキスト抽出
    text = get_webpage_text(url)      
    print("Webページからテキストを抽出しました")

    # 2. テキストをチャンクに分割
    chunks = split_into_chunks(text)  
    print(f"テキストを{len(chunks)}個のチャンクに分割しました")   # chunks は文字列のリスト

    # 3. チャンクをベクトル化
    chunk_embeddings = []
    for chunk in chunks:
        embedding = embed_text(client, chunk)  
        chunk_embeddings.append({   
            "text": chunk,
            "embedding": embedding
        })
    print("チャンクをベクトル化しました")
    # print(chunk_embeddings[:3])

    # 4. 関連チャンクを見つける
    relevant_chunks = find_relevant_chunks(client, question, chunk_embeddings)  
    print("質問に関連するチャンクを見つけました")   
    # print(relevant_chunks) 

    # 5. 回答を生成
    answer = generate_answer(client, question, relevant_chunks)  
    print("回答を生成しました")     # ここで実際に文章としての返答が生成

    return answer

if __name__ == "__main__":
    url = input("質問したいページの URL を入力してください:")
    question = input("質問を入力してください: ")
    answer = rag_qa(url, question)
    print("===== 回答 =====")
    print(answer)


# https://ja.wikipedia.org/wiki/メインページ
# このページの内容は？