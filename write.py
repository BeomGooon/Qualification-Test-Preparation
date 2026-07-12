import os
import json

file_path = "questions.json"

def write_question():
    new_data = {}
    print("문제의 중요도를 골라주십시오")
    inp = input().lower()
    if inp not in ['a', 'b', 'c']:
        print("문제 입력을 마무리하겠습니다.")
    else:
        new_data['importance'] = inp
        print("문제를 입력하세요. 문제 입력을 끝내려면 빈 줄에서 엔터(Enter)를 누르세요:")
        lines = []
        while True:
            line = input()
            if line == "":  # 아무것도 입력하지 않고 엔터만 누르면 루프 종료
                break
            lines.append(line)
        # 입력받은 모든 줄을 줄바꿈 문자(\n)로 이어붙입니다.
        final_string = "\n".join(lines)
        new_data['question'] = final_string
        print("답을 입력하세요. 답 입력을 끝내려면 빈 줄에서 엔터(Enter)를 누르세요:")
        lines = []
        while True:
            line = input().lower()
            if line == "":  # 아무것도 입력하지 않고 엔터만 누르면 루프 종료
                break
            lines.append(line)
        new_data['answer'] = lines
        print("교재 내 페이지를 입력하세요.(숫자만)")
        line = input()
        new_data['page'] = line
    return new_data


while True:
    # 1. 파일이 존재하는지 확인
    if os.path.exists(file_path):
        # 파일이 있으면 기존 데이터를 먼저 읽어옴
        with open(file_path, "r", encoding="utf-8") as file:
            try:
                data = json.load(file)
                # 기존 데이터가 리스트 형태라면 append, 딕셔너리라면 업데이트 등을 수행
                if isinstance(data, list):
                    new_data = write_question()
                    if new_data != {}:
                        data.append(new_data)
                else:
                    # 만약 기존 데이터가 단일 딕셔너리였다면 리스트로 묶어줌
                    new_data = write_question()
                    if new_data != {}:
                        data = [data, new_data]
            except json.JSONDecodeError:
                # 파일은 있지만 내용이 비어있거나 잘못된 경우
                new_data = write_question()
                if new_data != {}:
                    data = [new_data]
    else:
        # 2. 파일이 없으면 새로운 리스트로 시작
        new_data = write_question()
        if new_data != {}:
            data = [new_data]

    # 최종 데이터를 파일에 기록 ('w' 모드로 덮어써도 변수 data에 기존 내용이 포함되어 있음)
    if new_data != {}:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
    else:
        break