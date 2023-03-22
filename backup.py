import csv
import requests
import datetime
import schedule

def fgt_get_info():
    # 取得 fortigate api key 資訊
    with open('fgt_info.csv', 'r', newline='', encoding='utf-8-sig') as fgt_f:
        reader = csv.reader(fgt_f)
        info_list = []
        for info in reader:
            info_list.append(info)
    return info_list

def fgt_backup(ip_addr, api_key):
    # 登入備份設定欓
    api_url = f'https://{ip_addr}/api/v2/monitor/system/config/backup?scope=global&access_token={api_key}'
    requests.packages.urllib3.disable_warnings()
    data = requests.get(api_url, headers = {'User-agent': 'your bot 0.1'}, verify=False)
    today = datetime.date.today()
    if '200' in str(data):
        config_name = str(today) + '_' + ip_addr + '_api_configbackup.conf'
        with open(config_name ,'wb') as f:
            for line in data:
                f.write(line)
        print(ip_addr + ' Configuration backup OK!')
    else:
        print(ip_addr + ' Configuration backup Fail!')

def run():
    # 執行程式
    info_list = fgt_get_info()
    for fgt_info in info_list:
        fgt_ip = fgt_info[0]
        fgt_key = fgt_info[1]
        fgt_backup(fgt_ip, fgt_key)

schedule.every().day.at("15:10").do(run)

while True:
    schedule.run_pending()

