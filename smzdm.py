import requests, json,time,hashlib

#配置cookie 支持多账号一行一个 放单引号里面 根据实际需求增删
cookie = [
    '__ckguid=qYO2Qf9g1gIenv4yo4N8ll; device_id=21307064331673975655382201ebf0f12a5d1c097fd9a3c1a3e9ee082a; homepage_sug=a; r_sort_type=score; footer_floating_layer=0; sess=BA-1UTArRd5RkU8RyjhusDSlXvfqBvG%2FF8gyr21LNExNI99y6BidRAHcBDmJvnVfmV3Fn%2FFM7t865ioxMWn7SvXSRD%2BAweHWvAhtxXf7ylX2Tc4KHSFz%2FV5M1Vz; user=user%3A6997436914%7C6997436914; smzdm_id=6997436914; ad_date=22; bannerCounter=%5B%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%2C%7B%22number%22%3A0%2C%22surplus%22%3A1%7D%5D; ad_json_feed=%7B%7D; _zdmA.uid=ZDMA.Pj9j2ORIC.1674399839.2419200; _zdmA.vid=*; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22185c0b96fdb4b7-0b8d4652f72445-1a343370-2073600-185c0b96fdc2a2%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_landing_page%22%3A%22https%3A%2F%2Fwww.smzdm.com%2F%22%7D%2C%22%24device_id%22%3A%22185c0b96fdb4b7-0b8d4652f72445-1a343370-2073600-185c0b96fdc2a2%22%7D; Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58=1673975657,1674313764,1674399839; Hm_lpvt_9b7ac3d38f30fe89ff0b8a0546904e58=1674399839; _zdmA.time=1674399840104.0.https%3A%2F%2Fwww.smzdm.com%2F',
    '',
    ''
]

for i in range(len(cookie)):
    print(f'开始第{i + 1}个帐号签到')
    ts =int(round(time.time() * 1000))
    url = 'https://user-api.smzdm.com/robot/token'
    headers = {
        'Host': 'user-api.smzdm.com',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': f'{cookie[i]}',
        'User-Agent': 'smzdm_android_V10.4.1 rv:841 (22021211RC;Android12;zh)smzdmapp',
    }
    data={
        "f":"android",
        "v":"10.4.1",
        "weixin":1,
        "time":ts,
        "sign":hashlib.md5(bytes(f'f=android&time={ts}&v=10.4.1&weixin=1&key=apr1$AwP!wRRT$gJ/q.X24poeBInlUJC',encoding='utf-8')).hexdigest().upper()
    }
    html = requests.post(url=url, headers=headers, data=data)
    result = html.json()
    token= result['data']['token']

    Timestamp =int(round(time.time() * 1000))
    data={
        "f":"android",
        "v":"10.4.1",
        "sk":"ierkM0OZZbsuBKLoAgQ6OJneLMXBQXmzX+LXkNTuKch8Ui2jGlahuFyWIzBiDq/L",
        "weixin":1,
        "time":Timestamp,
        "token":token,
        "sign":hashlib.md5(bytes(f'f=android&sk=ierkM0OZZbsuBKLoAgQ6OJneLMXBQXmzX+LXkNTuKch8Ui2jGlahuFyWIzBiDq/L&time={Timestamp}&token={token}&v=10.4.1&weixin=1&key=apr1$AwP!wRRT$gJ/q.X24poeBInlUJC',encoding='utf-8')).hexdigest().upper()
    }
    url = 'https://user-api.smzdm.com/checkin'
    url2 = 'https://user-api.smzdm.com/checkin/all_reward'
    headers = {
        'Host': 'user-api.smzdm.com',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Cookie': f'{cookie[i]}',
        'User-Agent': 'smzdm_android_V10.4.1 rv:841 (22021211RC;Android12;zh)smzdmapp',
    }
    html = requests.post(url=url, headers=headers, data=data)
    html2 = requests.post(url=url2, headers=headers, data=data)
    result = json.loads(html.text)['error_msg']
    result2 = json.loads(html2.text)
    print(result)
    print(result2)
