import requests
import json

def get_data():

    url = "https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001"
    params = {
        "Authorization": "API授權碼",
        "locationName": "臺北市",
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = json.loads(response.text)

        location = data["records"]["location"][0]["locationName"]

        weather_elements = data["records"]["location"][0]["weatherElement"]
        start_time = weather_elements[0]["time"][0]["startTime"]
        end_time = weather_elements[0]["time"][0]["endTime"]
        weather_state = weather_elements[0]["time"][0]["parameter"]["parameterName"]
        rain_prob = weather_elements[1]["time"][0]["parameter"]["parameterName"]
        min_tem = weather_elements[2]["time"][0]["parameter"]["parameterName"]
        comfort = weather_elements[3]["time"][0]["parameter"]["parameterName"]
        max_tem = weather_elements[4]["time"][0]["parameter"]["parameterName"]

        print("地點：" + location)
        print("開始時間：" + start_time)
        print("結束時間：" + end_time)
        print("天氣描述：" + weather_state)
        print("降雨機率：" + rain_prob + "%")
        print("舒適度：" + comfort)
        print("最高溫：" + max_tem)
        print("最低溫：" + min_tem)

    else:
        print("Can't get data!")

if __name__ == '__main__':
    get_data()