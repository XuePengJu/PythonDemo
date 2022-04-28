# import logging
# import random
# import time
#
# from Python09FutureloanApiTestcaseDemo.api import *
#
# # 拼接手机号
# phone = "1{}{}{}".format([3, 5, 8][random.randint(0, 2)], [2, 3, 5, 7, 8, 9][random.randint(0, 5)],
#                          str(int(time.time()))[2::])
# res = register(phone, "1234567@", 1)
# logging.info("main test res.json = {} \n".format(res.json()))

json = {
    "code": 0,
    "msg": "OK",
    "data": {
        "id": 2,
        "leave_amount": 100,
        "mobile_phone": "13800000002",
        "reg_name": "Postman_t",
        "reg_time": "2022-04-26 10:38:51.0",
        "type": 0,
        "token_info": {
            "token_type": "Bearer",
            "expires_in": "2022-04-28 09:55:27",
            "token": "eyJhbGciOiJIUzUxMiJ9.eyJtZW1iZXJfaWQiOjIsImV4cCI6MTY1MTEzOTcyN30.h5_EJyUgjdN-j_o7P35ozaFlXq04P_O2ggIY3XUvRLgkA9Q_ct5WYdpaADBTz7GE5O4VFlBDiydkf-6wZOniKA"
        }
    },
    "copyright": "Copyright 柠檬班 © 2017-2020 湖南省零檬信息技术有限公司 All Rights Reserved"
}
print("原格式", json)
print("*** " * 100)
print(json.get("data").get("token_info").get("token"))
