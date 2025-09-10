def split_into_chunks(text, chunk_size=1000, overlap=200):    # テキストを指定サイズのチャンクに分割する関数
    if overlap >= chunk_size:   # 重なりは必ずチャンクサイズより小さくする必要がある
        raise ValueError("overlapはchunk_sizeより小さくしてください")

    chunks = []   # 空リスト
    start = 0     # 切出しの開始位置

    while start < len(text):
        end = min(start + chunk_size, len(text))  # 指定した長さ分切る、文章の最後を超えたらlen(text)にする

        # 文の途中で切れないように調整
        if end < len(text):
            temp_end = end
            while temp_end > start and text[temp_end] != ' ':
                temp_end -= 1
            if temp_end > start:
                end = temp_end  # 空白が見つかった場合のみ更新

        # チャンクを追加
        chunk = text[start:end].strip()   # start から end までの文字列を取り出して chunk とし、strip() で余分な空白を削除
        if not chunk:           # 空チャンクなら終了
            break
        chunks.append(chunk)    # それ以外はchunksに追加

        # 次のチャンクの開始位置（オーバーラップあり）
        new_start = end - overlap   # 次のチャンクは、現在のendから少し戻った位置から始める（= end - overlap）
        if new_start <= start:  # 進まない場合は強制的に進める
            new_start = start + chunk_size
        start = new_start

    return chunks