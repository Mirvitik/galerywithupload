import argparse

def calculate_profit_loss(args):
    # Определяем количество дней в каждом временном интервале
    days_in_year = 360
    days_in_month = 30
    days_in_week = 7

    # Инициализируем переменную для общего дохода/убытка
    total = 0.0

    # Считаем общий доход/убыток на основе входных аргументов
    if args.per_day is not None:
        total += args.per_day * 1  # 1 день
    if args.per_week is not None:
        total += args.per_week * (days_in_week / 1)  # Приводим к дням
    if args.per_month is not None:
        total += args.per_month * (days_in_month / 1)  # Приводим к дням
    if args.per_year is not None:
        total += args.per_year * (days_in_year / 1)  # Приводим к дням

    # Определяем, за какой период нужно рассчитать итог
    if args.get_by == 'day':
        return int(total)
    elif args.get_by == 'month':
        return int(total * (days_in_month / 1))  # Приводим к месяцам
    elif args.get_by == 'year':
        return int(total * (days_in_year / 1))  # Приводим к годам
    else:
        return int(total)  # По умолчанию считаем за день

def main():
    parser = argparse.ArgumentParser(description='Calculate Profit and Loss (P&L)')
    parser.add_argument('--per-day', type=float, help='Income/Expense per day')
    parser.add_argument('--per-week', type=float, help='Income/Expense per week')
    parser.add_argument('--per-month', type=float, help='Income/Expense per month')
    parser.add_argument('--per-year', type=float, help='Income/Expense per year')
    parser.add_argument('--get-by', choices=['day', 'month', 'year'], default='day',
                        help='Period to calculate P&L (default: day)')

    args = parser.parse_args()

    # Вычисляем и выводим итоговую сумму
    result = calculate_profit_loss(args)
    print(result)

if __name__ == '__main__':
    main()
