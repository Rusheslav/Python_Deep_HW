# Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

from datetime import datetime

balance = 0
note_mult = 50
pull_fee_rate = 1.5
pull_fee_min = 30
pull_fee_max = 600
interest = 3
wealth_tax = 10
wealth_limit = 5000000
counter = 3
list_of_operations = []


def change_balance(amt):
    if amt % note_mult:
        return 'Сумма не кратна 50'

    if - amt * pull_fee_rate / 100 >= pull_fee_max:
        pull_fee = - pull_fee_max
    elif pull_fee_min < - amt * pull_fee_rate / 100 < pull_fee_max:
        pull_fee = amt * pull_fee_rate / 100
    elif 0 < - amt * pull_fee_rate / 100 <= pull_fee_min:
        pull_fee = - pull_fee_min
    else:
        pull_fee = 0

    total_amt = amt + pull_fee

    global balance
    if balance > wealth_limit:
        balance -= balance * 0.1

    if balance + total_amt < 0:
        return f'На балансе недостаточно средств, что бы снять {-amt} у.е. и оплатить комиссию {-pull_fee} у.е.'

    balance += total_amt

    global counter
    counter -= 1

    if not counter:
        global interest
        balance += balance * interest / 100
        counter = 3

    return f'Остаток на балансе: {balance} у.е.\n'


amount = 1

while amount != 0:
    amount = int(input('Введите сумму, кратную 50 (положительную - для пополнения и отрицательную - для снятия со счёта).\n'
                       '0 - для выхода. \n'
                       '-: '))
    print(change_balance(amount))
    ct = datetime.now()
    if amount:
        list_of_operations.append(f'{ct}: изменение баланса на {amount} у.е. Новый баланс (с учетом налогов и комиссий):'
                              f' {balance}')

for i in list_of_operations:
    print(i)



