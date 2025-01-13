import csv
import requests
import numpy as np
from datetime import datetime, timedelta
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import matplotlib.ticker as ticker


class ThermalTime:
    def __init__(
        self, start_year, start_month, start_day, station_name, station_code, tb, theta
    ):
        self.start_year = start_year
        self.start_month = start_month
        self.start_day = start_day
        self.station_name = station_name
        self.station_code = station_code
        self.tb = tb
        self.theta = theta

    def deal_tx_max_abs_data(self):
        csv_url = f"https://agr.cwb.gov.tw/NAGR/history/station_day/create_report?station={self.station_code}&start_time=2017-01-01&end_time=2021-12-31&items=TxMaxAbs&report_type=csv&level={self.station_name}"

        with requests.Session() as s:
            download = s.get(csv_url)
            decoded_content = download.content.decode("utf-8", "ignore")
            cr = csv.reader(decoded_content.splitlines(), delimiter=",")
            my_list = list(cr)
            i = 1
            df = []
            # print(f"{station_code} 2017-01-01 to 2021-12-31 {report_items}\n")
            for row in my_list:
                jump = [
                    1,
                    2,
                    35,
                    36,
                    37,
                    38,
                    71,
                    72,
                    73,
                    74,
                    107,
                    108,
                    109,
                    110,
                    143,
                    144,
                    145,
                    146,
                    179,
                    180,
                ]
                if i not in jump:
                    df.append(row)
                i += 1

        data = np.zeros((5, 12, 31))
        for i in range(len(data)):
            for j in range(len(data[i])):
                for k in range(len(data[i][j])):
                    if (
                        df[32 * i + k + 1][j + 1] == "/"
                        or df[32 * i + k + 1][j + 1] == ""
                    ):
                        df[32 * i + k + 1][j + 1] = "0."

                    data[i][j][k] = float(df[32 * i + k + 1][j + 1])

        data_mean = np.zeros((12, 31))
        for j in range(len(data_mean)):
            for k in range(len(data_mean[j])):
                item = 0
                tmp_sum = 0.0
                for i in range(len(data)):
                    if data[i][j][k] != 0.0:
                        item += 1
                        tmp_sum += data[i][j][k]
                        # print(data[i][j][k])
                if item != 0:
                    data_mean[j][k] = tmp_sum / item
        self.t_max = data_mean

    def deal_TxMinAbs_data(self):
        csv_url = f"https://agr.cwb.gov.tw/NAGR/history/station_day/create_report?station={self.station_code}&start_time=2017-01-01&end_time=2021-12-31&items=TxMinAbs&report_type=csv&level={self.station_name}"

        with requests.Session() as s:
            download = s.get(csv_url)
            decoded_content = download.content.decode("utf-8", "ignore")
            cr = csv.reader(decoded_content.splitlines(), delimiter=",")
            my_list = list(cr)
            i = 1
            df = []
            # print(f"{station_code} 2017-01-01 to 2021-12-31 {report_items}\n")
            for row in my_list:
                jump = [
                    1,
                    2,
                    35,
                    36,
                    37,
                    38,
                    71,
                    72,
                    73,
                    74,
                    107,
                    108,
                    109,
                    110,
                    143,
                    144,
                    145,
                    146,
                    179,
                    180,
                ]
                if i not in jump:
                    df.append(row)
                i += 1

        data = np.zeros((5, 12, 31))
        for i in range(len(data)):
            for j in range(len(data[i])):
                for k in range(len(data[i][j])):
                    if (
                        df[32 * i + k + 1][j + 1] == "/"
                        or df[32 * i + k + 1][j + 1] == ""
                    ):
                        df[32 * i + k + 1][j + 1] = "0."

                    data[i][j][k] = float(df[32 * i + k + 1][j + 1])

        data_mean = np.zeros((12, 31))
        for j in range(len(data_mean)):
            for k in range(len(data_mean[j])):
                item = 0
                tmp_sum = 0.0
                for i in range(len(data)):
                    if data[i][j][k] != 0.0:
                        item += 1
                        tmp_sum += data[i][j][k]
                        # print(data[i][j][k])
                if item != 0:
                    data_mean[j][k] = tmp_sum / item
        self.t_min = data_mean

    def mgdd_list(self):
        mgdd = []
        for i in range(12):
            for j in range(31):
                if self.t_max[i][j] == 0.0:
                    continue
                elif i == 1 and j == 28:
                    continue
                if self.t_max[i][j] <= 30.0:
                    tmax = self.t_max[i][j]
                else:
                    tmax = 30.0
                if self.t_min[i][j] >= self.tb:
                    tmin = self.t_min[i][j]
                else:
                    tmin = self.tb
                T = (tmax + tmin) / 2
                mgdd.append(T - self.tb)
        self.mgdd = mgdd

    def start_day_Tsum(self):
        self.start_time = datetime(self.start_year, self.start_month, self.start_day)
        delta_days = (self.start_time - datetime(self.start_year, 1, 1)).days
        new_mgdd = self.mgdd[delta_days:] + self.mgdd[:delta_days]
        sigma_new_mgdd = []
        tsum = 0
        for i in range(len(new_mgdd)):
            tsum += new_mgdd[i]
            sigma_new_mgdd.append(tsum)
        # print(sigma_new_mgdd)
        self.sigma_new_mgdd = sigma_new_mgdd

    def fdd_NewtInt(self):
        self.x = np.array([0, 100, 200, 300, 364])
        self.y = np.array(
            [
                0,
                self.sigma_new_mgdd[99],
                self.sigma_new_mgdd[199],
                self.sigma_new_mgdd[299],
                self.sigma_new_mgdd[363],
            ]
        )
        self.n = len(self.x) - 1
        fdd = np.zeros((self.n + 1, self.n + 1))
        for i in range(self.n + 1):
            fdd[i][0] = self.y[i]
        for j in range(1, self.n + 1):
            for i in range(self.n - j + 1):
                fdd[i][j] = (fdd[i + 1][j - 1] - fdd[i][j - 1]) / (
                    self.x[i + j] - self.x[i]
                )
        self.f = fdd[0]

    def output_days(self):
        def f_x(n, xi, x, yint, f, theta):
            xterm = 1
            yint[0] = f[0]
            for order in range(1, n):
                xterm = xterm * (xi - x[order - 1])
                yint2 = yint[order - 1] + f[order] * xterm
                yint[order] = yint2
            return yint[n - 1] - theta

        def f_1x(xi, f):
            tmp_sum = 0.0
            tmp_sum += float(f[1])
            tmp_sum += float(f[2]) * (2 * xi - 100)
            tmp_sum += float(f[3]) * (3 * xi ** (2) - 600 * xi + 20000)
            tmp_sum += float(f[4]) * (
                4 * xi ** (3) - 1800 * xi ** (2) + 220000 * xi - 6000000
            )
            return tmp_sum

        yint = np.zeros(self.n)
        self.old_x = 1
        while True:
            self.new_x = self.old_x - f_x(
                self.n, self.old_x, self.x, yint, self.f, self.theta
            ) / f_1x(self.old_x, self.f)
            if (self.new_x - self.old_x) / self.new_x <= 0.000005:
                break
            else:
                self.old_x = self.new_x

    def print_forecast_harvest_date(self):
        end_time = self.start_time + timedelta(days=int(np.ceil(self.new_x)))
        print("預計完成日:", end_time.strftime("%Y-%m-%d"))

    def plot(self):
        x_time = []
        time = self.start_time
        for i in range(len(self.sigma_new_mgdd)):
            x_time.append(time)  # .strftime('%Y-%m-%d'))
            time += timedelta(days=1)

        fig, ax = plt.subplots()
        ax.plot(x_time, self.sigma_new_mgdd)

        ax.xaxis.set_major_locator(dates.MonthLocator())
        ax.xaxis.set_minor_locator(dates.MonthLocator(bymonthday=12))

        ax.xaxis.set_major_formatter(ticker.NullFormatter())
        ax.xaxis.set_minor_formatter(dates.DateFormatter("%b"))

        ax.tick_params(axis="x", which="minor", tick1On=False, tick2On=False)

        # Align the minor tick label
        for label in ax.get_xticklabels(minor=True):
            label.set_horizontalalignment("center")
        plt.show()


station_name = [
    "蘭陽分場",
    "花蓮農改",
    "台東茶改",
    "台中農改",
    "農業試驗所",
    "雲林分場",
    "義竹分場",
    "高雄農改",
    "旗南農改",
    "畜試所",
    "桃園農改",
]
station_code = [
    "72U480",
    "72T250",
    "82S580",
    "72G600",
    "G2F820",
    "72K220",
    "72M360",
    "72Q010",
    "72V140",
    "B2N890",
    "72C440",
]
# ThernalTime(start_year, start_month, start_day, station_name, station_code, tb, theta)
abc = ThermalTime(2022, 6, 1, "臺中農改", "72G600", 10, 1100)
abc.deal_tx_max_abs_data()
abc.deal_TxMinAbs_data()
abc.mgdd_list()
abc.start_day_Tsum()
abc.fdd_NewtInt()
abc.output_days()
abc.print_forecast_harvest_date()
abc.plot()
