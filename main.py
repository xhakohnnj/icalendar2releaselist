import sys
from enum import IntEnum
from module import UrlToDataList


# 引数
class Args(IntEnum):
  OUTPUT_FILE   = 1   # 出力ファイル
  DATE_START    = 2   # 日付の範囲(開始)
  DATE_END      = 3   # 日付の範囲(終了)

# リリースカレンダー
url = "https://calendar.google.com/calendar/ical/i3h9mf13qmbe2qq927gaadagfg%40group.calendar.google.com/public/basic.ics"
# ゲームパス IN
#url = "https://calendar.google.com/calendar/ical/1eef2cc17a7eb797b59c0f59cee0bef68cae4ccf20e58b3a6798441773933f0b%40group.calendar.google.com/public/basic.ics"
# ゲームパス OUT
#url = "https://calendar.google.com/calendar/ical/c04a293ee84ddbbfb3a54a8150be8a35a768dd19616b4174c6fe97ebf8aa8409%40group.calendar.google.com/public/basic.ics"

data_list = UrlToDataList.Main( url, sys.argv[Args.DATE_START], sys.argv[Args.DATE_END] )


output_file = open( sys.argv[Args.OUTPUT_FILE], mode='w', encoding='utf-8', newline='\n' )

for data in data_list:
  item = '{0}　{1}'.format( data.date.strftime('%m/%d'), data.title )
  if not data.options == None and 0 < len(data.options): # なんかNoneじゃなくて空白も入ってるところもあるのでlenでもチェック.
    item += '　{0}'.format( data.options )
  print( item )
  if not output_file is None:
    output_file.write( item + '\n' )
