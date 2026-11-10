
from quiz import Quiz


def get_default_quizzes():
    return [
        Quiz(
            "Python에서 변수를 선언하는 올바른 방법은?",
            ["var x = 10", "x = 10", "int x = 10", "let x = 10"],
            2
        ),
        Quiz(
            "Python에서 리스트를 만드는 기호는?",
            ["{}", "()", "[]", "<>"],
            3
        ),
        Quiz(
            "조건문을 작성할 때 사용하는 키워드는?",
            ["for", "if", "while", "def"],
            2
        ),
        Quiz(
            "Python에서 함수를 정의하는 키워드는?",
            ["func", "function", "define", "def"],
            4
        ),
        Quiz(
            "반복 실행에 사용할 수 있는 키워드는?",
            ["for", "class", "import", "return"],
            1
        )
    ]
