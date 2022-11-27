#
# iCalendarからリリースデータのリストに変換
# URL指定版.
#
from enum import IntEnum, auto
from datetime import datetime
import urllib.request
from .lib import iCalLib
from . import Datas

# データの配列のインデックス
class eDataSourceIndex(IntEnum):
  Date = 0 # 最初のauto()は1になるとのことで。
  Name = auto()
  Options = auto()


#
# main
#
def Main( url, date_start_str, date_end_str ):

  # 文字列から日付に変換
  def StrToDate( str ):
    return datetime.strptime( str.replace('/','-'),'%Y-%m-%d' )

  lines = None
  with urllib.request.urlopen(url) as f:
    lines = f.readlines()
  if lines is None:
    return None

  ical_data = []
  for line in lines:
    ical_data.append( line.decode().strip() )
  del lines # 必要なくなったので破棄しておく

  date_start = StrToDate( date_start_str )
  date_end = StrToDate( date_end_str )

  # 元データを作成
  data_sources = []
  data_source = None # あまり凝らずにとりあえず配列で.
  for item in ical_data:
    if iCalLib.HasTag(item,iCalLib.eTag.Begin):
      data_source = [None,None,None] # eDataIndexと合わせる
    elif iCalLib.HasTag(item,iCalLib.eTag.End):
      data_sources.append( data_source )
      data_source = None
    elif iCalLib.HasTag(item,iCalLib.eTag.DateStart):
      data_source[eDataSourceIndex.Date] = datetime.strptime( iCalLib.GetTagValue(item), '%Y%m%d' )
    elif iCalLib.HasTag(item,iCalLib.eTag.Summary):
      data_source[eDataSourceIndex.Name] = iCalLib.GetTagValue( item )
    elif iCalLib.HasTag(item,iCalLib.eTag.Description):
      data_source[eDataSourceIndex.Options] = iCalLib.GetTagValue( item )
  
  # iCalに登録されてるのが日付順じゃないのでソートする.
  data_sources.sort()

  release_title_data_list = []
  for data_source in data_sources:
    # 日付の範囲
    if not date_start <= data_source[eDataSourceIndex.Date] <= date_end:
      continue

    release_title_data_list.append(
      Datas.ReleaseData(
        data_source[eDataSourceIndex.Date]
        , data_source[eDataSourceIndex.Name]
        , data_source[eDataSourceIndex.Options]
      )
    )

  return release_title_data_list
