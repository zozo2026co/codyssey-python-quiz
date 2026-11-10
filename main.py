
from quiz_data import get_default_quizzes


def show_menu():
    print("\n===== 나만의 퀴즈 게임 =====")
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")


def play_quiz():
    quizzes = get_default_quizzes()

    if not quizzes:
        print("등록된 퀴즈가 없습니다.")
        return

    score = 0

    for index, quiz in enumerate(quizzes, start=1):
        print(f"\n[문제 {index}]")
        quiz.display()

        while True:
            answer = input("정답 입력 (1-4): ").strip()

            if not answer:
                print("정답을 입력해주세요.")
                continue

            try:
                answer = int(answer)
            except ValueError:
                print("숫자를 입력해주세요.")
                continue

            if 1 <= answer <= 4:
                break

            print("1~4 사이의 번호를 입력해주세요.")

        if quiz.check_answer(answer):
            print("정답입니다!")
            score += 1
        else:
            print(f"오답입니다. 정답은 {quiz.answer}번입니다.")

    print(f"\n결과: {len(quizzes)}문제 중 {score}문제 정답")



def main():
    while True:
        try:
            show_menu()
            choice = input("메뉴 선택 (1-5): ").strip()

            if not choice:
                print("번호를 입력해주세요.")
            elif choice == "1":
                play_quiz()
            elif choice in ("2", "3", "4"):
                print("아직 준비 중인 기능입니다.")
            elif choice == "5":
                print("게임을 종료합니다.")
                break
            else:
                print("1~5 사이의 번호를 입력해주세요.")

        except (KeyboardInterrupt, EOFError):
            print("\n안전하게 프로그램을 종료합니다.")
            break


if __name__ == "__main__":
    main()
