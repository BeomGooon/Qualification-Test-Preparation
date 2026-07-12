import os
import json

file_path = "questions.json"
new_data = {"name": "이순신", "age": 40, "city": "부산"}

# 1. 파일이 존재하는지 확인
if os.path.exists(file_path):
    # 파일이 있으면 기존 데이터를 먼저 읽어옴
    with open(file_path, "r", encoding="utf-8") as file:
        try:
            data = json.load(file)
            # 기존 데이터가 리스트 형태라면 append, 딕셔너리라면 업데이트 등을 수행
            if isinstance(data, list):
                data.append(new_data)
            else:
                # 만약 기존 데이터가 단일 딕셔너리였다면 리스트로 묶어줌
                data = [data, new_data]
        except json.JSONDecodeError:
            # 파일은 있지만 내용이 비어있거나 잘못된 경우
            data = [new_data]
else:
    # 2. 파일이 없으면 새로운 리스트로 시작
    data = [new_data]

# 최종 데이터를 파일에 기록 ('w' 모드로 덮어써도 변수 data에 기존 내용이 포함되어 있음)
with open(file_path, "w", encoding="utf-8") as file:
    json.dump(data, file, indent=4, ensure_ascii=False)