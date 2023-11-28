import requests
import copy
import json

class GPTService:
    _instance = None
    _url = 'https://estsoft-openai-api.jejucodingcamp.workers.dev/'

    _data = []
    _data.append({
        "role" :  "system",
        "content" : "assistant는 투자 전문가이다.",
    })

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(GPTService, cls).__new__(cls)

        return cls._instance
    
    def Analysis(self, cotent):
        headers = {'Content-Type': 'application/json'}
        data = copy.deepcopy(self._data)
        data.append({
            "role" :  "user",
            "content" : f"주어진 댓글을 토대로 해당 투자자의 투자 심리를 분석해줘. 마지막에 요약해서 이 사람의 투자 심리를 반드시 다음 3개 중에서 '중립적', '긍정적', '부정적' 선택해줘. ``` 댓글 : {cotent}```",
        })

        response = requests.post(self._url, json=data, headers=headers)
        print(response.text)
        if response.status_code != 200:
            return None
        
        return json.loads(response.text)