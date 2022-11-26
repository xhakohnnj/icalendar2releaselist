import sys
from enum import IntEnum
from module import UrlToDataList


# 引数
class Args(IntEnum):
  DATE_START = 1    # 日付の範囲(開始)
  DATE_END = 2      # 日付の範囲(終了)

url = "https://calendar.google.com/calendar/ical/i3h9mf13qmbe2qq927gaadagfg%40group.calendar.google.com/public/basic.ics"

data_list = UrlToDataList.Main( url, sys.argv[Args.DATE_START], sys.argv[Args.DATE_END] )
for data in data_list:
  item = '{0}　{1}'.format( data.date.strftime('%m/%d'), data.title )
  if data.options != None:
    item += '　{0}'.format( data.options )
  print( item )
