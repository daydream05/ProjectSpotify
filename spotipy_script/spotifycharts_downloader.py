import os
import pandas as pd
import urllib.request

dir_path = os.getcwd()
project_dir = os.path.abspath(os.path.join(dir_path, os.pardir))

def download_daily_per_region():
    country_names = pd.read_csv("country_names.csv")
    # This returns a DateTimeIndex, we need to turn it into a string with just the  year
    date = pd.date_range('2015-09-01', '2016-09-01')
    dates = date.strftime("%Y-%m-%d")

    url = "https://spotifycharts.com/regional/"
    for name in country_names['code']:
        print("Downloading files from " + name)
        frames = []

        for date in dates:
            complete_url = url +  name + "/daily/" + date + "/download"
            #try:
                #daily = pd.read_csv(url)
                #print('read succesful')
                #daily['code'] = name
                #daily['date'] = date
                #frames.append(daily)

            daily = pd.read_csv(complete_url, error_bad_lines=False)
            daily['code'] = name
            daily['date'] = date
            frames.append(daily)

            #except urllib.request.HTTPError as err:
            #print(err)
        result = pd.concat(frames)

        result.to_csv(project_dir + "\\spotipy_script\\country\\" + name + ".csv")
        print("Finished downloading files from" + name)


if __name__ == '__main__':
    print("Program starting...")
    download_daily_per_region()



