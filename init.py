import urllib.request
import json
import requests
# pip install requests で　requestsモジュールのインストールをしておくこと

#----------file情報取得--------------
#channelのTokenを指定する
url = 'https://slack.com/api/files.list?token={0}&pretty=1&page={1}'.format('token', 1)
response = requests.get(url)
data = response.json()
#最後の[0]をしているしないと['channelId'] 指定するとchannelId　が返ってくる
channel = data['files'][0]['channels'][0]
print(channel)
#----------file取得--------------

##----------ファイル削除クエリ----------
##----------ファイル削除クエリ----------

#----------postMessage---------------
#パラメータ用意
url = 'https://slack.com/api/chat.postMessage'
#botのTokenを指定する
headers = {
    'Authorization': 'Bearer token',
    'Content-Type': 'application/json; charset=utf-8'
}
method = 'POST'
data = {
    "channel": channel,
    "username": "Slack監視bot",
    "text": "ファイルの共有は規約により禁止されています。削除しました。",
}
json_data = json.dumps(data).encode("utf-8")

#リクエスト
req = urllib.request.Request(url=url, data=json_data, headers=headers, method=method)
res = urllib.request.urlopen(req, timeout=5)

#レスポンス表示
print("Http status: {0} {1}".format(res.status, res.reason))
print(res.read().decode("utf-8"))
#----------postMessage---------------