import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("country_population.csv")
data2 = pd.read_csv("fertility_rate.csv")
data3 = pd.read_csv("life_expectancy.csv")

years = ['1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974',
                 '1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989',
                 '1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004',
                 '2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016' ]


def showGraph(self,country,year) :
    try:
        self.Country = country
        self.Year = year
        dataf = data[data["Country Name"] == self.Country][self.Year].item()
        datan = dataf/10000
        plt.title(country + "'s Population",fontname="Comic Sans MS", fontsize=16)
        plt.xlabel("Year",fontname="Comic Sans MS", fontsize=16)
        plt.ylabel("Population/10000",fontname="Comic Sans MS", fontsize=16)

        i = [self.Year]
        ax = plt.bar(i,datan)
        label_bar(plt, ax, str(dataf), is_inside=True, color="white")
        fig = plt.gcf()
        fig.canvas.set_window_title('Population Graph Section')
        plt.show()
    except BaseException as ex:
        print(ex)

def label_bar(ax, bars, text_format, is_inside=True, **kwargs):
    """
    Attach a text label to each bar displaying its y value
    """
    max_y_value = max(bar.get_height() for bar in bars)
    if is_inside:
        distance = max_y_value * 0.05
    else:
        distance = max_y_value * 0.01

    for bar in bars:
        text = text_format.format(bar.get_height())
        text_x = bar.get_x() + bar.get_width() / 2
        if is_inside:
            text_y = bar.get_height() - distance
        else:
            text_y = bar.get_height() + distance

        ax.text(text_x, text_y, text, ha='center', va='bottom', **kwargs)


def showGraphFertility(self,country,year) :
    try:
        self.Country = country
        self.Year = year
        data9 = data2[data2["Country Name"] == self.Country][self.Year].item()
        plt.title(country + "'s Fertility Rate", fontname="Comic Sans MS", fontsize=20)
        plt.xlabel("Year" , fontname="Comic Sans MS", fontsize=16)
        plt.ylabel("Fertility Rate" , fontname="Comic Sans MS", fontsize=16)
        i = [self.Year]
        ax = plt.bar(i, data9)
        label_bar(plt, ax, str(data9), is_inside=True, color="white")
        fig = plt.gcf()
        fig.canvas.set_window_title('Fertility Rate Graph Section')
        plt.show()
    except BaseException as ex:
        print(ex)


def showGraphLife(self,country,year) :
    try:
        self.Country = country
        self.Year = year
        data7 = data3[data3["Country Name"] == self.Country][self.Year].item()
        plt.title(country + "'s Life Expectancy Rate" , fontname="Comic Sans MS", fontsize=20)
        plt.xlabel("Year" , fontname="Comic Sans MS", fontsize=16)
        plt.ylabel("Life Expectancy Rate" , fontname="Comic Sans MS", fontsize=16)
        i = [self.Year]
        ax = plt.bar(i, data7)
        label_bar(plt, ax, str(data7), is_inside=True, color="white")
        fig = plt.gcf()
        fig.canvas.set_window_title('Life Expectancy Rate Graph Section')
        plt.show()
    except BaseException as ex:
        print(ex)


def viewGraphPopulation(self, country):
    try:
        self.Country = country
        d = data.index[data["Country Name"] == self.Country].tolist()

        fig, (ax1, ax2, ax3) = plt.subplots(3, sharey=False)

        ax1.plot(data.iloc[d[0], 4:23])
        ax1.set_ylabel("Population", fontname="Comic Sans MS", fontsize=16)
        ax1.set_title((self.Country + "'s Population"), fontname="Comic Sans MS", fontsize=22)
        ax1.legend([self.Country])

        ax2.plot(data.iloc[d[0], 23:42])
        ax2.set_ylabel("Population", fontname="Comic Sans MS", fontsize=16)

        ax3.plot(data.iloc[d[0], 42:61])
        ax3.set_xlabel("Years", fontname="Comic Sans MS", fontsize=16)
        ax3.set_ylabel("Population", fontname="Comic Sans MS", fontsize=16)

        fig = plt.gcf()
        fig.canvas.set_window_title('Population Graph Section')

        plt.show()

    except BaseException as ex:
        print(ex)


def viewGraphFertility(self,country) :
    try:
        self.Country = country
        d = data.index[data["Country Name"] == self.Country].tolist()

        fig, (ax1, ax2, ax3) = plt.subplots(3, sharey=False)

        ax1.plot(data.iloc[d[0], 4:23])
        ax1.set_ylabel("Fertility Rate", fontname="Comic Sans MS", fontsize=16)
        ax1.set_title((self.Country + "'s Fertility Rate"), fontname="Comic Sans MS", fontsize=22)
        ax1.legend([self.Country])

        ax2.plot(data.iloc[d[0], 23:42])
        ax2.set_ylabel("Fertility Rate", fontname="Comic Sans MS", fontsize=16)

        ax3.plot(data.iloc[d[0], 42:61])
        ax3.set_xlabel("Years", fontname="Comic Sans MS", fontsize=16)
        ax3.set_ylabel("Fertility Rate", fontname="Comic Sans MS", fontsize=16)

        fig = plt.gcf()
        fig.canvas.set_window_title('Fertility Rate Graph Section')

        plt.show()

    except BaseException as ex:
        print(ex)


def viewGraphLife(self, country):
    try:
        self.Country = country
        d = data.index[data["Country Name"] == self.Country].tolist()

        fig, (ax1, ax2, ax3) = plt.subplots(3, sharey=False)

        ax1.plot(data.iloc[d[0], 4:23])
        ax1.set_ylabel("Life Expectancy", fontname="Comic Sans MS", fontsize=16)
        ax1.set_title((self.Country + "'s Life Expectancy Rate"), fontname="Comic Sans MS", fontsize=22)
        ax1.legend([self.Country])

        ax2.plot(data.iloc[d[0], 23:42])
        ax2.set_ylabel("Life Expectancy", fontname="Comic Sans MS", fontsize=16)

        ax3.plot(data.iloc[d[0], 42:61])
        ax3.set_xlabel("Years", fontname="Comic Sans MS", fontsize=16)
        ax3.set_ylabel("Life Expectancy", fontname="Comic Sans MS", fontsize=16)

        fig = plt.gcf()
        fig.canvas.set_window_title('Life Expectancy Rate Graph Section')

        plt.show()

    except BaseException as ex:
        print(ex)



def barGraph1(self ,country1,country2):
    try:
        self.Country1 = country1
        self.Country2 = country2
        d = data.index[data["Country Name"] == self.Country1].tolist()
        d1 = data.index[data["Country Name"] == self.Country2].tolist()
        fig, (ax1, ax2, ax3) = plt.subplots(3, sharey=False)
        d5 = data.iloc[d[0], 4:23]
        d6 = data.iloc[d1[0], 4:23]
        d7 = data.iloc[d[0], 23:42]
        d8 = data.iloc[d1[0], 23:42]
        d9 = data.iloc[d[0], 42:61]
        d10 = data.iloc[d1[0], 42:61]
        width = 0.35
        li = []
        li2 = []
        li3 = []
        li4 = []
        li5 = []
        li6 = []
        for val in d5:
            li.append(val)
        i = d5.keys()
        for val in d6:
            li2.append(val)
        i2 = d6.keys()

        for val in d7:
            li3.append(val)
        i3 = d7.keys()
        for val in d8:
            li4.append(val)
        i4 = d8.keys()

        for val in d9:
            li5.append(val)
        i5 = d9.keys()
        for val in d10:
            li6.append(val)
        i6 = d10.keys()

        rects1 = ax1.bar(i, li, -width, align='edge', color='r')
        rects2 = ax1.bar(i2, li2, +width, align='edge', color='y')

        rects3 = ax2.bar(i3, li3, -width, align='edge', color='r')
        rects4 = ax2.bar(i4, li4, +width, align='edge', color='y')

        rects5 = ax3.bar(i5, li5, -width, align='edge', color='r')
        rects6 = ax3.bar(i6, li6, +width, align='edge', color='y')

        ax1.legend([self.Country1, self.Country2])
        ax1.set_ylabel("Population", fontname="Comic Sans MS", fontsize=16)
        ax1.set_title('Population Graph of ' + self.Country1 + ' and ' + self.Country2, fontname="Comic Sans MS", fontsize=22)

        ax2.set_ylabel("Population", fontname="Comic Sans MS", fontsize=16)

        ax3.set_xlabel("Years", fontname="Comic Sans MS", fontsize=16)
        ax3.set_ylabel("Population", fontname="Comic Sans MS", fontsize=16)

        fig = plt.gcf()
        fig.canvas.set_window_title('Population Graphical Analysis Section')
        plt.show()

    except BaseException as ex:
        print(ex)


def barGraph2(self ,country1,country2):
    try:
        self.Country1 = country1
        self.Country2 = country2
        d = data2.index[data2["Country Name"] == self.Country1].tolist()
        d1 = data2.index[data2["Country Name"] == self.Country2].tolist()
        fig, (ax1, ax2, ax3) = plt.subplots(3, sharey=False)
        d5 = data.iloc[d[0], 4:23]
        d6 = data.iloc[d1[0], 4:23]
        d7 = data.iloc[d[0], 23:42]
        d8 = data.iloc[d1[0], 23:42]
        d9 = data.iloc[d[0], 42:61]
        d10 = data.iloc[d1[0], 42:61]
        width = 0.35
        li = []
        li2 = []
        li3 = []
        li4 = []
        li5 = []
        li6 = []
        for val in d5:
            li.append(val)
        i = d5.keys()
        for val in d6:
            li2.append(val)
        i2 = d6.keys()

        for val in d7:
            li3.append(val)
        i3 = d7.keys()
        for val in d8:
            li4.append(val)
        i4 = d8.keys()

        for val in d9:
            li5.append(val)
        i5 = d9.keys()
        for val in d10:
            li6.append(val)
        i6 = d10.keys()

        rects1 = ax1.bar(i, li, -width, align='edge', color='r')
        rects2 = ax1.bar(i2, li2, +width, align='edge', color='y')

        rects3 = ax2.bar(i3, li3, -width, align='edge', color='r')
        rects4 = ax2.bar(i4, li4, +width, align='edge', color='y')

        rects5 = ax3.bar(i5, li5, -width, align='edge', color='r')
        rects6 = ax3.bar(i6, li6, +width, align='edge', color='y')

        ax1.legend([self.Country1, self.Country2])
        ax1.set_ylabel("Fertility Rate", fontname="Comic Sans MS", fontsize=16)
        ax1.set_title('Fertility Rate Graph of ' + self.Country1 + ' and ' + self.Country2, fontname="Comic Sans MS", fontsize=22)

        ax2.set_ylabel("Fertility Rate", fontname="Comic Sans MS", fontsize=16)

        ax3.set_xlabel("Years", fontname="Comic Sans MS", fontsize=16)
        ax3.set_ylabel("Fertility Rate", fontname="Comic Sans MS", fontsize=16)

        fig = plt.gcf()
        fig.canvas.set_window_title('Fertility Rate Graphical Analysis Section')
        plt.show()

    except BaseException as ex:
        print(ex)


def barGraph3(self ,country1,country2):
    try:
        self.Country1 = country1
        self.Country2 = country2
        d = data3.index[data3["Country Name"] == self.Country1].tolist()
        d1 = data3.index[data3["Country Name"] == self.Country2].tolist()
        fig, (ax1, ax2, ax3) = plt.subplots(3, sharey=False)
        d5 = data.iloc[d[0], 4:23]
        d6 = data.iloc[d1[0], 4:23]
        d7 = data.iloc[d[0], 23:42]
        d8 = data.iloc[d1[0], 23:42]
        d9 = data.iloc[d[0], 42:61]
        d10 = data.iloc[d1[0], 42:61]
        width = 0.35
        li = []
        li2 = []
        li3 = []
        li4 = []
        li5 = []
        li6 = []
        for val in d5:
            li.append(val)
        i = d5.keys()
        for val in d6:
            li2.append(val)
        i2 = d6.keys()

        for val in d7:
            li3.append(val)
        i3 = d7.keys()
        for val in d8:
            li4.append(val)
        i4 = d8.keys()

        for val in d9:
            li5.append(val)
        i5 = d9.keys()
        for val in d10:
            li6.append(val)
        i6 = d10.keys()

        rects1 = ax1.bar(i, li, -width, align='edge', color='r')
        rects2 = ax1.bar(i2, li2, +width, align='edge', color='y')

        rects3 = ax2.bar(i3, li3, -width, align='edge', color='r')
        rects4 = ax2.bar(i4, li4, +width, align='edge', color='y')

        rects5 = ax3.bar(i5, li5, -width, align='edge', color='r')
        rects6 = ax3.bar(i6, li6, +width, align='edge', color='y')

        ax1.legend([self.Country1, self.Country2])
        ax1.set_ylabel("Life Expectancy", fontname="Comic Sans MS", fontsize=16)
        ax1.set_title('Life Expectancy Graph of ' + self.Country1 + ' and ' + self.Country2, fontname="Comic Sans MS", fontsize=22)

        ax2.set_ylabel("Life Expectancy", fontname="Comic Sans MS", fontsize=16)

        ax3.set_xlabel("Years", fontname="Comic Sans MS", fontsize=16)
        ax3.set_ylabel("Life Expectancy", fontname="Comic Sans MS", fontsize=16)

        fig = plt.gcf()
        fig.canvas.set_window_title('Life Expectancy Rate Graphical Analysis Section')
        plt.show()

    except BaseException as ex:
        print(ex)




# THESE ARE THE COMPARISON GRAPHS

def Graph1(self,country1,country2,year) :
    try:
        self.country1 = country1
        self.country2 = country2
        self.year = year
        data9 = data[data["Country Name"] == self.country1][self.year].item()
        data10 = data[data["Country Name"] == self.country2][self.year].item()

        df = pd.DataFrame({'Country Name': [self.country1, self.country2], 'census': [data9/10000, data10/10000]})
        ax = df.plot.bar(x='Country Name', y='census', rot=0)
        ax.set_title("Population In Year " + self.year , fontname="Comic Sans MS" , fontsize=22 )
        ax.set_xlabel("Country Name", fontname="Comic Sans MS" , fontsize=18)
        ax.set_ylabel("Population/10000", fontname="Comic Sans MS" , fontsize=18)
        #label_bar(plt, ax, 'Country Name', is_inside=True, color="white")

        plt.show()

    except BaseException as ex:
            print(ex)


def Graph2(self,country1,country2,year) :
    try:
        self.country1 = country1
        self.country2 = country2
        self.year = year
        data9 = data2[data2["Country Name"] == self.country1][self.year].item()
        data10 = data2[data2["Country Name"] == self.country2][self.year].item()

        df = pd.DataFrame({'Country Name': [self.country1, self.country2], 'rate': [data9, data10]})
        ax = df.plot.bar(x='Country Name', y='rate', rot=0)
        ax.set_title("Fertility Rate In Year " + self.year , fontname="Comic Sans MS" , fontsize=22 )
        ax.set_xlabel("Country Name", fontname="Comic Sans MS" , fontsize=18)
        ax.set_ylabel("Fertility Rate", fontname="Comic Sans MS" , fontsize=18)

        plt.show()

    except BaseException as ex:
        print(ex)


def Graph3(self,country1,country2,year) :
    try:
            self.country1 = country1
            self.country2 = country2
            self.year = year
            data7 = data3[data3["Country Name"] == self.country1][self.year].item()
            data8 = data3[data3["Country Name"] == self.country2][self.year].item()

            df = pd.DataFrame({'Country Name': [self.country1, self.country2], 'rate': [data7, data8]})
            ax = df.plot.bar(x='Country Name', y='rate', rot=0)
            ax.set_title("Life Expectancy In Year " + self.year , fontname="Comic Sans MS" , fontsize=22 )
            ax.set_xlabel("Country Name", fontname="Comic Sans MS" , fontsize=18)
            ax.set_ylabel("Life Expectancy", fontname="Comic Sans MS" , fontsize=18)

            plt.show()

    except BaseException as ex:
            print(ex)

def Graph4(self, country, year1, year2):
    try:
            self.country = country
            self.year1 = year1
            self.year2 = year2
            data2 = data[data["Country Name"] == self.country][self.year1].item()
            data3 = data[data["Country Name"] == self.country][self.year2].item()

            df = pd.DataFrame({'Year Name': [self.year1, self.year2], 'census': [data2/10000, data3/10000]})
            ax = df.plot.bar(x='Year Name', y='census', rot=0)
            ax.set_title("Population of " + self.country, fontname="Comic Sans MS", fontsize=22)
            ax.set_xlabel("Year", fontname="Comic Sans MS", fontsize=18)
            ax.set_ylabel("Population/10000", fontname="Comic Sans MS", fontsize=18)

            plt.show()

    except BaseException as ex:
            print(ex)

def Graph5(self, country, year1, year2):
    try:
            self.country = country
            self.year1 = year1
            self.year2 = year2
            data9 = data2[data2["Country Name"] == self.country][self.year1].item()
            data10 = data2[data2["Country Name"] == self.country][self.year2].item()

            df = pd.DataFrame({'Year Name': [self.year1, self.year2], 'rate': [data9, data10]})
            ax = df.plot.bar(x='Year Name', y='rate', rot=0)
            ax.set_title("Fertility Rate of " + self.country, fontname="Comic Sans MS", fontsize=22)
            ax.set_xlabel("Year", fontname="Comic Sans MS", fontsize=18)
            ax.set_ylabel("Fertility Rate", fontname="Comic Sans MS", fontsize=18)

            plt.show()

    except BaseException as ex:
            print(ex)

def Graph6(self, country, year1, year2):
    try:
            self.country = country
            self.year1 = year1
            self.year2 = year2
            data7 = data3[data3["Country Name"] == self.country][self.year1].item()
            data8 = data3[data3["Country Name"] == self.country][self.year2].item()

            df = pd.DataFrame({'Year Name': [self.year1, self.year2], 'rate': [data7, data8]})
            ax = df.plot.bar(x='Year Name', y='rate', rot=0)
            ax.set_title("Life Expectancy of " + self.country, fontname="Comic Sans MS", fontsize=22)
            ax.set_xlabel("Year", fontname="Comic Sans MS", fontsize=18)
            ax.set_ylabel("Life Expectancy", fontname="Comic Sans MS", fontsize=18)

            plt.show()

    except BaseException as ex:
            print(ex)



def Graph7(self, country1 , country2):
    try:
        self.Country1 = country1
        self.Country2 = country2
        d1 = data.index[data["Country Name"] == self.Country1].tolist()
        d2 = data.index[data["Country Name"] == self.Country2].tolist()

        fig, (ax1, ax2, ax3) = plt.subplots(3, sharey=False)

        ax1.plot(data.iloc[d1[0], 4:23])
        ax1.plot(data.iloc[d2[0], 4:23])
        ax1.set_ylabel("Population", fontname="Comic Sans MS", fontsize=16)
        ax1.set_title("Population Comparison", fontname="Comic Sans MS", fontsize=22)
        ax1.legend([self.Country1, self.Country2])

        ax2.plot(data.iloc[d1[0], 23:42])
        ax2.plot(data.iloc[d2[0], 23:42])
        ax2.set_ylabel("Population", fontname="Comic Sans MS", fontsize=16)
        ax2.legend([self.Country1, self.Country2])

        ax3.plot(data.iloc[d1[0], 42:61])
        ax3.plot(data.iloc[d2[0], 42:61])
        ax3.set_xlabel("Years", fontname="Comic Sans MS", fontsize=16)
        ax3.set_ylabel("Population", fontname="Comic Sans MS", fontsize=16)
        ax3.legend([self.Country1, self.Country2])

        fig = plt.gcf()
        fig.canvas.set_window_title('Population Graph Section')

        plt.show()

    except BaseException as ex:
        print(ex)


def Graph8(self,country1,country2) :
    try:
        self.Country1 = country1
        self.Country2 = country2
        d1 = data2.index[data2["Country Name"] == self.Country1].tolist()
        d2 = data2.index[data2["Country Name"] == self.Country2].tolist()

        fig, (ax1, ax2, ax3) = plt.subplots(3, sharey=False)

        ax1.plot(data2.iloc[d1[0], 4:23])
        ax1.plot(data2.iloc[d2[0], 4:23])
        ax1.set_ylabel("Fertility Rate", fontname="Comic Sans MS", fontsize=16)
        ax1.set_title("Fertility Rate Comparison", fontname="Comic Sans MS", fontsize=22)
        ax1.legend([self.Country1, self.Country2])

        ax2.plot(data2.iloc[d1[0], 23:42])
        ax2.plot(data2.iloc[d2[0], 23:42])
        ax2.set_ylabel("Fertility Rate", fontname="Comic Sans MS", fontsize=16)
        ax1.legend([self.Country1, self.Country2])

        ax3.plot(data2.iloc[d1[0], 42:61])
        ax3.plot(data2.iloc[d2[0], 42:61])
        ax3.set_xlabel("Years", fontname="Comic Sans MS", fontsize=16)
        ax3.set_ylabel("Fertility Rate", fontname="Comic Sans MS", fontsize=16)
        ax3.legend([self.Country1, self.Country2])

        fig = plt.gcf()
        fig.canvas.set_window_title('Fertility Rate Graph Section')

        plt.show()

    except BaseException as ex:
        print(ex)


def Graph9(self, country1,country2):
    try:
        self.Country1 = country1
        self.Country2 = country2
        d1 = data3.index[data3["Country Name"] == self.Country1].tolist()
        d2 = data3.index[data3["Country Name"] == self.Country2].tolist()

        fig, (ax1, ax2, ax3) = plt.subplots(3, sharey=False)

        ax1.plot(data3.iloc[d1[0], 4:23])
        ax1.plot(data3.iloc[d2[0], 4:23])
        ax1.set_ylabel("Life Expectancy", fontname="Comic Sans MS", fontsize=16)
        ax1.set_title( "Life Expectancy Rate Comparison", fontname="Comic Sans MS", fontsize=22)
        ax1.legend([self.Country1, self.Country2])

        ax2.plot(data3.iloc[d1[0], 23:42])
        ax2.plot(data3.iloc[d2[0], 23:42])
        ax2.set_ylabel("Life Expectancy", fontname="Comic Sans MS", fontsize=16)
        ax2.legend([self.Country1, self.Country2])

        ax3.plot(data3.iloc[d1[0], 42:61])
        ax3.plot(data3.iloc[d2[0], 42:61])
        ax3.set_xlabel("Years", fontname="Comic Sans MS", fontsize=16)
        ax3.set_ylabel("Life Expectancy", fontname="Comic Sans MS", fontsize=16)
        ax3.legend([self.Country1, self.Country2])

        fig = plt.gcf()
        fig.canvas.set_window_title('Life Expectancy Rate Graph Section')

        plt.show()

    except BaseException as ex:
        print(ex)
