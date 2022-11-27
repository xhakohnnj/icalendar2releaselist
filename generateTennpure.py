#
# テンプレ出力
# 
import sys
from enum import IntEnum
from module import UrlToDataList
from module.tennpure import DataListTo as GenerateTennpureTo


# 引数
class Args(IntEnum):
  OUTPUT_FILE   = 1   # 出力ファイル
  DATE_START    = 2   # 日付の範囲(開始)
  DATE_END      = 3   # 日付の範囲(終了)

# 各種URL定義
# リリースカレンダー
url_release_calendar = "https://calendar.google.com/calendar/ical/i3h9mf13qmbe2qq927gaadagfg%40group.calendar.google.com/public/basic.ics"
# ゲームパス IN
url_gamepass_in = "https://calendar.google.com/calendar/ical/1eef2cc17a7eb797b59c0f59cee0bef68cae4ccf20e58b3a6798441773933f0b%40group.calendar.google.com/public/basic.ics"
# ゲームパス OUT
url_gamepass_out = "https://calendar.google.com/calendar/ical/c04a293ee84ddbbfb3a54a8150be8a35a768dd19616b4174c6fe97ebf8aa8409%40group.calendar.google.com/public/basic.ics"


# リリースカレンダー
release_list = UrlToDataList.Main( url_release_calendar, sys.argv[Args.DATE_START], sys.argv[Args.DATE_END] )
# ゲームパス IN
gamepass_in_list = UrlToDataList.Main( url_gamepass_in, sys.argv[Args.DATE_START], sys.argv[Args.DATE_END] )
# ゲームパス OUT
gamepass_out_list = UrlToDataList.Main( url_gamepass_out, sys.argv[Args.DATE_START], sys.argv[Args.DATE_END] )

# テンプレ出力
with open( sys.argv[Args.OUTPUT_FILE], mode='w', encoding='utf-8', newline='\n' ) as output_file:
  GenerateTennpureTo.File( output_file, release_list, gamepass_in_list, gamepass_out_list )
