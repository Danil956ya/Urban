def check_validation(sender):
    validations_ends = (".com", ".ru", ".net")
    return "@" in sender and str(sender).endswith(validations_ends)

def send_email(message, recipient, sender = "university.help@gmail.com"):
    if check_validation(recipient) and check_validation(sender):
        if str(recipient) == str(sender):
            print("Нельзя отправить письмо самому себе!")
            return
        if sender == "university.help@gmail.com":
            print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
            return
        else:
            print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")
            return
    else:
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
    return

send_email("Привет!", "university.help@dawd.ru", "university.help@dawd.ru")