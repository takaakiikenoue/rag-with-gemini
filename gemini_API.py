import os
from dotenv import load_dotenv
import google.genai as genai

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")  # 取得
if not api_key:
    raise ValueError("環境変数 GOOGLE_API_KEY が設定されていません")

client = genai.Client(api_key=api_key)