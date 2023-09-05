# Возьмите задачу о банкомате из семинара 2. 
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

START_BALANCE = 0
DEPOSIT_FACTOR = 50
WITHDRAW_FACTOR = 50
WITHDRAW_RATE = 0.015
WITHDRAW_RATE_MIN = 30
WITHDRAW_RATE_MAX = 600
INTEREST_FREQUENCY = 3
INTEREST_PERCENT = 0.003
THRESHOLD_AMOUNT = 5_000_000
WEALTH_TAX = 0.010

# Функции для операций счета
def deposit(account_balance, operations):
    deposit_amount = get_valid_input(f'Введите сумму пополнения, кратную {DEPOSIT_FACTOR}: ', DEPOSIT_FACTOR)
    account_balance += deposit_amount
    operations.append(deposit_amount)
    return account_balance

def withdraw(account_balance, operations):
    withdraw_amount = get_valid_input(f'Введите сумму снятия, кратную {WITHDRAW_FACTOR}.\nНельзя снять больше, чем на счете: ', WITHDRAW_FACTOR)
    percent = calculate_withdraw_percent(account_balance)
    if withdraw_amount + percent > account_balance:
        print('Недостаточно средств на счете')
    else:
        account_balance -= withdraw_amount + percent
        operations.append(-withdraw_amount - percent)
    return account_balance

def calculate_withdraw_percent(balance):
    percent = balance * WITHDRAW_RATE
    return max(min(percent, WITHDRAW_RATE_MAX), WITHDRAW_RATE_MIN)

def calculate_interest(account_balance):
    return account_balance * INTEREST_PERCENT

def apply_wealth_tax(account_balance):
    if account_balance > THRESHOLD_AMOUNT:
        tax = account_balance * WEALTH_TAX
        account_balance -= tax
        print(f'Удержан налог на богатство: {tax:.0f}')
    return account_balance

def get_valid_input(prompt, factor):
    while True:
        amount = int(input(prompt))
        if amount > 0 and amount % factor == 0:
            return amount
        else:
            print(f'Сумма должна быть положительной и кратной {factor}')

# Основной код
balance = START_BALANCE
operations = []

while True:
    balance = apply_wealth_tax(balance)
    if len(operations) % INTEREST_FREQUENCY == 0:
        interest = calculate_interest(balance)
        balance += interest
        operations.append(interest)

    action = input('Для работы с банкоматом выберите действие:\n1 - пополнить\n2 - снять\n3 - выйти\n')
    if action == '1':
        balance = deposit(balance, operations)
    elif action == '2':
        balance = withdraw(balance, operations)
    elif action == '3':
        print(f'Баланс вашего счета: {balance:.0f}')
        break
    else:
        print('Некорректное действие')

print(operations)