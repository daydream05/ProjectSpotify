import os
import pandas as pd
import urllib.request

dir_path = os.getcwd()
project_dir = os.path.abspath(os.path.join(dir_path, os.pardir))

def save_file(code, url, csv_name):
    filepath = os.path.join(os.path.dirname(os.path.abspath(__file__)), "save_here", "country", code)

    if not os.path.exists(filepath):
        os.makedirs(filepath)



    number_of_files = len([name for name in os.listdir(filepath) if os.path.isfile(os.path.join(filepath, name))])

    if number_of_files != 367:
        filename = os.path.join(filepath, csv_name)
        urllib.request.urlretrieve(url, filename)


def open_url_list():
    csv = os.path.join(project_dir, "all_download_url.csv")
    url_df = pd.read_csv(csv)

    for index, row in url_df.iterrows():
        code = row['code']
        date = row['date']
        url = row['url']

        csv_name = ''
        #creates a name for our csv file with the format YYY-m-d-code.csv
        csv_name = csv_name.join([url.split('/')[6], '-', code, '.csv'])
        save_file(code, url, csv_name)


if __name__ == '__main__':
    print("Program starting...")
    open_url_list()