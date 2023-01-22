import requests, demjson ,re,time,json

# 推送不加了感觉没啥用
# 把值得买的cookie放入下面的单引号里面  有几个帐号就弄几个（默认设置了3个 根据自己情况改）
cookie_list = ['__ckguid=qYO2Qf9g1gIenv4yo4N8ll; device_id=21307064331673975655382201ebf0f12a5d1c097fd9a3c1a3e9ee082a; homepage_sug=a; r_sort_type=score; footer_floating_layer=0; sess=BA-1UTArRd5RkU8RyjhusDSlXvfqBvG/F8gyr21LNExNI99y6BidRAHcBDmJvnVfmV3Fn/FM7t865ioxMWn7SvXSRD+AweHWvAhtxXf7ylX2Tc4KHSFz/V5M1Vz; user=user:6997436914|6997436914; smzdm_id=6997436914; ad_date=22; bannerCounter=[{"number":0,"surplus":1},{"number":0,"surplus":1},{"number":0,"surplus":1},{"number":0,"surplus":1},{"number":0,"surplus":1},{"number":0,"surplus":1}]; ad_json_feed={}; _zdmA.uid=ZDMA.Pj9j2ORIC.1674399839.2419200; _zdmA.vid=*; sensorsdata2015jssdkcross={"distinct_id":"185c0b96fdb4b7-0b8d4652f72445-1a343370-2073600-185c0b96fdc2a2","first_id":"","props":{"$latest_traffic_source_type":"直接流量","$latest_search_keyword":"未取到值_直接打开","$latest_referrer":"","$latest_landing_page":"https://www.smzdm.com/"},"$device_id":"185c0b96fdb4b7-0b8d4652f72445-1a343370-2073600-185c0b96fdc2a2"}; Hm_lvt_9b7ac3d38f30fe89ff0b8a0546904e58=1673975657,1674313764,1674399839; Hm_lpvt_9b7ac3d38f30fe89ff0b8a0546904e58=1674399839; _zdmA.time=1674399840104.0.https://www.smzdm.com/','','']
# 活动id
active_id = ['ljX8qVlEA7','AlZE6eX8Ky']


for i in range(len(cookie_list)):
    for a in range(len(active_id)):
        projectList = []
        url = f'https://zhiyou.smzdm.com/user/lottery/jsonp_draw?active_id={active_id[a]}'
        rewardurl= f'https://zhiyou.smzdm.com/user/lottery/jsonp_get_active_info?active_id={active_id[a]}'
        infourl = 'https://zhiyou.smzdm.com/user/'
        headers = {
            'Host': 'zhiyou.smzdm.com',
            'Accept': '*/*',
            'Connection': 'keep-alive',
            'Cookie': cookie_list[i],
            'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148/smzdm 10.4.6 rv:130.1 (iPhone 13; iOS 15.6; zh_CN)/iphone_smzdmapp/10.4.6/wkwebview/jsbv_1.0.0',
            'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
            'Referer': 'https://m.smzdm.com/',
            'Accept-Encoding': 'gzip, deflate, br'
        }
        response = requests.post(url=url, headers=headers).text
        response_info = requests.get(url=infourl, headers=headers).text
        response_reward = requests.get(url=rewardurl, headers=headers)
        result_reward = json.loads(response_reward.text)
        name = str(re.findall('<a href="https://zhiyou.smzdm.com/user"> (.*?) </a>', str(response_info), re.S)).replace('[','').replace(']','').replace('\'','')
        level = str(re.findall('<img src="https://res.smzdm.com/h5/h5_user/dist/assets/level/(.*?).png\?v=1">', str(response_info), re.S)).replace('[','').replace(']','').replace('\'','')
        gold = str(re.findall('<div class="assets-part assets-gold">\n                    (.*?)</span>', str(response_info), re.S)).replace('[','').replace(']','').replace('\'’','').replace('<span class="assets-part-element assets-num">','').replace('\'','')
        silver = str(re.findall('<div class="assets-part assets-prestige">\n                    (.*?)</span>', str(response_info), re.S)).replace('[','').replace(']','').replace('\'’','').replace('<span class="assets-part-element assets-num">','').replace('\'','')
        data = demjson.decode(str(response), encoding='utf-8')
        print('帐号' + str(i + 1)+ ' VIP'+ level + ' ' + name + ' ' + data['error_msg']+'  剩余碎银 '+silver +'  剩余金币 '+ gold)
        time.sleep(2)
