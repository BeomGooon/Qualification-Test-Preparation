import json
import random

def run_quiz(file_path):
    # 1. JSON 파일 로드
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"오류: '{file_path}' 파일을 찾을 수 없습니다.")
        return
    except json.JSONDecodeError:
        print("오류: JSON 파일 형식이 올바르지 않습니다.")
        return

    # JSON 데이터가 리스트 형식이라고 가정합니다.
    # 만약 특정 key 안에 리스트가 있다면 data['key_name'] 형태로 수정해야 합니다.
    if not isinstance(data, list):
        print("오류: JSON의 최상위 데이터 구조가 리스트가 아닙니다.")
        return

    answer = input("중요도가 A인 문제만 보겠습니까?(y) 아니면 B인 문제도 같이 보겠습니까?(n)\n")
    if answer == "y":
        # 2. 'importance'가 'a'인 개체만 필터링
        filtered_questions = [item for item in data if item.get('importance') == 'a']
    elif answer == "n":
        # 2. 'importance'가 'a', 'b'인 개체만 필터링
        filtered_questions = [item for item in data if item.get('importance') in ['a', 'b']]
    else:
        print("잘못된 입력을 하셨습니다. 종료하겠습니다.")
        return -1

    if not filtered_questions:
        if answer == "y":
            print("'importance'가 'a'인 문제를 찾을 수 없습니다.")
        elif answer == "n":
            print("'importance'가 'a', 'b'인 문제를 찾을 수 없습니다.")
        return

    # 3. 리스트를 무작위로 섞음 (결국 끝까지 모두 뽑게 됨)
    random.shuffle(filtered_questions)

    print(f"총 {len(filtered_questions)}개의 문제를 시작합니다!\n")
    correct_count = 0

    # 4. 루프를 돌며 문제 출제 및 입력 확인
    for idx, item in enumerate(filtered_questions, 1):
        question = item.get('question', '문제가 없습니다.')
        answers = item.get('answer', [])
        page = item.get('page', 0)

        # answer가 리스트 형태가 아니라면 리스트로 변환 (예외 방지)
        if not isinstance(answers, list):
            answers = [answers]

        print(f"[문제 {idx}] {question}")
        user_input = input("정답을 입력하세요: ").strip()

        # 사용자의 입력이 answer 리스트에 있는지 확인
        if user_input in answers:
            print("▶ 정답입니다! ✨")
            print(f"해당 문제는 교재 {page}p에 있습니다.")
            correct_count += 1
        else:
            print(f"▶ 틀렸습니다. 😢 (인정되는 정답: {', '.join(map(str, answers))})")
            print(f"해당 문제는 교재 {page}p에 있습니다.")
        print("-" * 40)

    print(f"\n퀴즈가 끝났습니다! 맞힌 개수: {correct_count} / {len(filtered_questions)}")

# 코드 실행 (파일명이 'questions.json'인 경우)
if __name__ == "__main__":
    run_quiz('questions.json')