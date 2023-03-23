from calculate_date_total import calculate_totals
from parcer import parse_excel_file

FILE_NAME = 'Приложение_к_заданию_бек_разработчика.xlsx'

if __name__ == "__main__":
    parse_excel_file(FILE_NAME)
    calculate_totals()
