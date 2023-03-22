# FortiGate Configuration Backup Tool
## 安裝說明
### 需求
- Python 3.9
- Install libary
    ```
    cd FGT_BackupConfig_API
    pip install -r requirements.txt
    ```
### 使用方式
1. `git clone https://github.com/viviol-lu/FGT_BackupConfig_API.git` 將檔案下載
2. 將 fortigate 的 IP & API key 寫到 `fgt_info.csv` 中
3. 程式已設定每日 15:10 進行備份，若要修改時間，backup.py 第 38 行，將 15:10 改成想要的時間
4. 執行程式 `python backup.py`

## 設定
### CSV 格式
```
FGT_IP,FGT_API_KEY
```
> 如果 port 號不是 443，FGT_IP 的欄位寫 <IP>:<PORT> 的格式，例如 192.168.1.99:8443

### 產生 API Key
- `System > Administrators > Created New > REST API Admin` 設定 API Account</br>
![CleanShot 2023-03-22 at 09 18 32](https://user-images.githubusercontent.com/69979158/226832299-c5f33248-0f60-468b-8506-fa9d19856463.png)
- 設定 `Username`、`Administrator Profile`、`Trusted Hosts`，完成後按下 `OK`，其中，Administrator Profile 需要是 <font color=red>read/write 權限</font></br>
![CleanShot 2023-03-22 at 09 24 29](https://user-images.githubusercontent.com/69979158/226832413-4e8d1a45-2d00-4b9e-b075-4b45f859f20b.png)
![CleanShot 2023-03-22 at 13 57 47](https://user-images.githubusercontent.com/69979158/226832555-73142fbc-d16d-4446-853a-da70cb0a6d66.png)
- 按下完成後會取得一組 API key，該 key 要儲存好</br>
![CleanShot 2023-03-22 at 09 27 26](https://user-images.githubusercontent.com/69979158/226832651-550a4522-109a-46fa-8fca-9433bcec5d0b.png)
- 如果是 vdom 環境，要登入下以下指令
```
config system accprofile
edit api_read_write
set scope global
```
- PC 上 `curl -k -i -X POST https://x.x.x.x/logincheck -d "username=api_test&secretkey=zzz" --dump-header headers.txt -c cookies.txt` 可以測試 api 連線狀態
	- `x.x.x.x`：FortiGate 帳號
	- `zzz`：API key
	- `headers.txt`：header 資訊儲存
	- `cookies.txt`：cookie 資訊儲存
  
 
