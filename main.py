from datetime import datetime

import matplotlib.dates as mdates
import matplotlib.pyplot as plt


# Question 1
def read_close_data():
    close_list_2018 = []
    close_list_2019 = []
    months_2018 = []
    months_2019 = []

    with open('data/DAT_XLSX_EURUSD_M1_2018.csv', 'r') as f:
        lines = f.readlines()
        for line in lines:
            close_list_2018.append(float((line.split(';')[4]).replace(',', '.')))
            months_2018.append(line.split(';')[0])

    with open('data/DAT_XLSX_EURUSD_M1_2019.csv', 'r') as f:
        lines = f.readlines()
        for line in lines:
            close_list_2019.append(float((line.split(';')[4]).replace(',', '.')))
            months_2019.append(line.split(';')[0])

    return close_list_2018, close_list_2019, months_2018, months_2019

def draw_graph():
    close_point_2018, close_point_2019, months_2018, months_2019 = read_close_data()
    x_axis_2018 = [datetime.strptime(d, '%Y-%m-%d %H:%M').date() for d in months_2018]
    x_axis_2019 = [datetime.strptime(d, '%Y-%m-%d %H:%M').date() for d in months_2019]

    fig, ax = plt.subplots()
    ax.plot(x_axis_2018, close_point_2018, label='2018')
    ax.plot(x_axis_2019, close_point_2019, label='2019')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%m'))
    ax.xaxis.set_major_locator(mdates.MonthLocator())
    ax.set_xlabel('Months')
    ax.set_ylabel('Close')
    ax.set_title('Close price evolution during 2018 and 2019')
    ax.legend()
    plt.show()


if __name__ == '__main__':
    # Question 1
    draw_graph()

