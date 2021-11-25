per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input("Введите сумму денег"))
percent_values = list(per_cent.values())
deposit = []
for i in percent_values:
    deposit.append((i*money)/100)#так и не придумал варианта проще, кроме цикла, чтобы проумножать все элементы списка сразу.
print("проценты по данному вкладу будут равны:", list(map(round, deposit)))
print('Максимальная сумма, которую вы можете заработать —', max(list(map(round, deposit))))

#альтернативный длинный метод (видимо, правильный)
deposit_TKB = int(per_cent['ТКБ']*money/100)
deposit_SKB = int(per_cent['СКБ']*money/100)
deposit_VTB = int(per_cent['ВТБ']*money/100)
deposit_SBER = int(per_cent['СБЕР']*money/100)
deposit_full = deposit_SBER, deposit_VTB, deposit_SKB, deposit_TKB
print("Альтернативный подход по подсчету процентов:", deposit_full)
maximum_profit = max(deposit_full)
print('Максимальная сумма, которую вы можете заработать —', maximum_profit)




