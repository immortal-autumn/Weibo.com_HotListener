import requests, pandas, json, time
from bs4 import BeautifulSoup


url = "https://s.weibo.com/top/summary?cate=realtimehot"
path = "/var/www/html/WeiboData/"


def record_real_hot():
    hot = []
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, features="html.parser")

    for i in soup.select('.td-02 > a[target="_blank"]'):
        hot.append(i.get_text())
    return hot


def record_to_file(filename, content_rec):
    print(content_rec)
    with open(f'{path}{filename}.json', 'w+', encoding='utf-8') as f:
        json.dump(content_rec, f, ensure_ascii=False)


if __name__ == '__main__':
    new_day = True
    while True:
        local_time = time.localtime(time.time())
        if local_time.tm_hour < 5:
            new_day = True
        if local_time.tm_hour == 17 and new_day:
            name = time.strftime("%Y_%m_%d_%H_%M_%S", local_time)
            record_to_file(name, record_real_hot())
            new_day = False
        time.sleep(3600)
        # record_real_hot()

