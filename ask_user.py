small_talk_dict = {"Как дела?": "Хорошо!",
                   "Что делаешь?": "Программирую",
                   "Когда спать пойдешь?": "Ближе к утру"}


def get_answer(question, answers):
    if question in answers:
        return answers.get(question)
    else:
        return "..."


def ask_user(answers):
    try:
        while True:
            user_say = input("Поговори со мной... ")
            if user_say == "Пока!":
                break
            else:
                reply = get_answer(user_say, answers)
                print(reply)

    except KeyboardInterrupt:
        print("\nПока!")


ask_user(small_talk_dict)

