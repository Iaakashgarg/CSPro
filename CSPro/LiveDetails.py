import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

def func():
    try:
        page = requests.get('http://worldpopulationreview.com/')
        soup = BeautifulSoup(page.text, 'html.parser')
        world_list = soup.find(class_='table table-striped')
        new = world_list.find('tbody')
        c_name = []
        cp = []
        np = []
        nnp = []
        gr = []
        rank = []

        for row in new.find_all('tr'):
            col = row.find_all('td')

            column_2 = col[1].text.strip()
            c_name.append(column_2)

            column_3 = col[2].text.strip()
            cp.append(column_3)

            column_4 = col[3].text.strip()
            np.append(column_4)

            column_5 = col[4].text.strip()
            nnp.append(column_5)

            column_6 = col[5].text.strip()
            gr.append(column_6)

            column_7 = col[6].text.strip()
            rank.append(column_7)

        columns = {'Country Name': c_name, 'Current Population': cp, 'Expected Population': np, 'New Population': nnp
            , 'Growth Rate': gr, 'Rank': rank}
        df = pd.DataFrame(columns)
        return  df
        #print(df.head(30))

    except BaseException as ex:
        print(ex)


def MainGraph(self,country):
    try:
        self.country = country
        data = func()
        data1 = data[data["Country Name"] == self.country]["Current Population"].item()
        data2 = data[data["Country Name"] == self.country]["Expected Population"].item()
        data3 = data[data["Country Name"] == self.country]["New Population"].item()
        d1 = int(data1.replace(',', ''))
        d2 = int(data2.replace(',', ''))
        d3 = int(data3.replace(',', ''))

        df = pd.DataFrame({'Name': ["Current Population", "Population 2030", "Population 2050"], 'census': [d1/10000, d2/10000, d3/10000]})
        ax = df.plot.bar(x='Name', y='census', rot=0)
        ax.set_title("Population of " + self.country, fontname="Comic Sans MS", fontsize=22)
        ax.set_xlabel(self.country, fontname="Comic Sans MS", fontsize=18)
        ax.set_ylabel("Population/10000", fontname="Comic Sans MS", fontsize=18)
        fig = plt.gcf()
        fig.canvas.set_window_title('Live Population Graph Section')
        plt.show()

    except BaseException as ex:
        print(ex)
