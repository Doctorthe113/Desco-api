# Made by The Doctor
# https://pypi.org/project/descoApi/0.1/
from urllib import response
from requests import get

# balance_url = "http://prepaid.desco.org.bd/api/tkdes/customer/getBalance?accountNo=" # 1234567
# monthly_consume = "http://prepaid.desco.org.bd/api/tkdes/customer/getCustomerMonthlyConsumption?accountNo=" # 1234567&meterNo=&monthFrom=2021-08&monthTo=2022-07
# daily_consume = "http://prepaid.desco.org.bd/api/tkdes/customer/getCustomerDailyConsumption?accountNo=" # 1234567&meterNo=&dateFrom=2023-07-31&dateTo=2023-08-29
# recharge_history = "http://prepaid.desco.org.bd/api/tkdes/customer/getRechargeHistory?accountNo=" # 1234567&meterNo=&dateFrom=2022-08-01&dateTo=2023-07-31

# def check_balance(account):
#     url = balance_url + str(account)
#     response = requests.get(url).json()

#     balance = response["data"]["balance"]
#     current_month_consume = response["data"]["currentMonthConsumption"]
#     return balance, current_month_consume

# def monthly_consumption(account, month):
#     monthFrom = f"&monthFrom={month}&monthTo={month}"
#     url = monthly_consume + str(account) + monthFrom
#     response = requests.get(url).json()

#     consumed_taka = response["data"][0]["consumedTaka"]
#     consumed_unit = response["data"][0]["consumedUnit"]
#     return consumed_taka, consumed_unit

# def daily_consumption(account, date):
#     days = str.split(date, "-")
#     day = days[:2] # this keeps only the year and the month
#     day.append(str(int(days[2]) - 1))
#     modified_date = "-".join(day) # all this to get the previous day

#     dateFrom = f"&dateFrom={modified_date}&dateTo={date}"
#     url = daily_consume + str(account) + dateFrom
#     response = requests.get(url).json()

#     previous_day_consumed_taka = response["data"][0]["consumedTaka"]
#     consumed_taka_upto_today = response["data"][1]["consumedTaka"]
#     previous_day_consumed_unit = response["data"][0]["consumedUnit"]
#     consumed_unit_upto_today = response["data"][1]["consumedUnit"]

#     consumed_taka = int(consumed_taka_upto_today) - int(previous_day_consumed_taka)
#     consumed_unit = int(consumed_unit_upto_today) - int(previous_day_consumed_unit)

#     return consumed_taka_upto_today, consumed_unit_upto_today, consumed_taka, consumed_unit

# def last_recharge(account, date):
#     days = str.split(date, "-")
#     day = days[1] # this gets the month and saves it in "day" variable for later use
#     del days[1]
#     days.insert(1, format(int(day) - 1, "02d"))
#     modified_date = "-".join(days) # all this to get the previous month

#     dateFrom = f"&dateFrom={modified_date}&dateTo={date}"
#     url = recharge_history + str(account) + dateFrom
#     response = requests.get(url).json()

#     recharge_date = response["data"][0]["rechargeDate"]
#     recharge_amount = response["data"][0]["totalAmount"]
#     order_id = response["data"][0]["orderID"]

#     return recharge_date, recharge_amount, order_id










class descoAPI():
    def __init__(self, accountNumber: int) -> None:
        self.balanceURL = "http://prepaid.desco.org.bd/api/tkdes/customer/getBalance?"
        self.monthlyConsume = "http://prepaid.desco.org.bd/api/tkdes/customer/getCustomerMonthlyConsumption?"
        self.dailyConsume = "http://prepaid.desco.org.bd/api/tkdes/customer/getCustomerDailyConsumption?"
        self.recharge = "http://prepaid.desco.org.bd/api/tkdes/customer/getRechargeHistory?"
        self.account = accountNumber

    def balanceCheck(self) -> int:
        response = get(self.balanceURL, params={"accountNo": self.account}).json()
        balance = response["data"]
        return balance

    def monthlyCheck(self, monthFrom, monthTo) -> str:
        response = get(self.monthlyConsume, params={"accountNo": self.account, "monthFrom": monthFrom, "monthTo": monthTo}).json()
        balance = response["data"]
        return balance

    def datecheck(self, dateFrom, dateTo) -> str:
        response = get(self.dailyConsume, params={"accountNo": self.account, "dateFrom": dateFrom, "dateTo": dateTo}).json()
        balance = response["data"]
        return balance

    def rechargeHistory(self, dateFrom, dateTo) -> str:
        response = get(self.recharge, params={"accountNo": self.account, "dateFrom": dateFrom, "dateTo": dateTo}).json()
        balance = response["data"]
        return balance

    def help(self):
        print(f"\033[35m 1. \033[37m \033[36m \'balanceCheck\' \033[0m Returns a json containing balance and monthly consumption upto today.")
        print(f"\033[35m 2. \033[37m \033[36m \'monthlyCheck\' \033[0m Returns a json for all info from \'monthFrom\' to \'monthTo\'. Max range 12 months.")
        print(f"\033[35m 3. \033[37m \033[36m \'dateCheck\' \033[0m Returns a json for all info from \'dateFrom\' to \'dateTo\'. Max range 30 days.")
        print(f"\033[35m 3. \033[37m \033[36m \'rechargeHistory\' \033[0m Returns a json for all info from \'dateFrom\' to \'dateTo\'. Max range 30 days. Only show the running month\'s info.")
        return f"\033[31m \033[4m For any issues or questions contact via GitHub. \033[0m"


print(descoAPI(12021574).help())