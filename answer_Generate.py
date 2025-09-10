def generate_answer(client, question, relevant_chunks):

    # print("=== DEBUG generate_answer ===")
    # print("type of relevant_chunks:", type(relevant_chunks))
    # if isinstance(relevant_chunks, list):
    #     print("list length:", len(relevant_chunks))
    #     print("first element type:", type(relevant_chunks[0]))
    #     print("first element content:", relevant_chunks[0])
    # else:
    #     print("relevant_chunks content:", relevant_chunks)

    # コンテキストを作成
    context = "\n\n".join([str(chunk["text"]) for chunk in relevant_chunks]) # チャンクごとのテキストをまとめて一つの文字列にする。\n\n で区切って改行を入れることで、モデルが読みやすくしている
    prompt = f"""以下は、Webページから抽出された情報です：
            {context}
            上記の情報をもとに、次の質問に答えてください：

            {question}
            できるだけ与えられた情報のみを使って回答してください。
            情報が不足している場合は、「提供された情報からは回答できません」と答えてください。
            """

    # Gemini で回答生成
    response = client.models.generate_content(
        model="gemini-1.5-flash", # 使用モデルの推定
        contents=prompt,
        config={
            "temperature": 0.3, 
        }
    )
    if hasattr(response, "text"):
        return response.text
    elif hasattr(response, "candidates"):
        return response.candidates[0].content.parts[0].text
    else:
        return str(response)
    # return response.text
