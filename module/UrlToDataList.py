from enum import IntEnum, auto
from datetime import datetime
import urllib.request
from .lib import iCalLib
from .data import ReleaseTitleData


class eDataIndex(IntEnum):
  Date = 0 # 最初のauto()は1になるとのことで。
  Name = auto()
  Options = auto()


# main
def Main( url ):

  lines = None
  with urllib.request.urlopen(url) as f:
    lines = f.readlines()
  if lines is None:
    return None

  ical_data = []
  for line in lines:
    ical_data.append( line.decode().strip() )
  del lines # 必要なくなったので削除しておく
  
  # 簡単なデータを先に作りたい
  data_sources = []
  data_source = None
  for item in ical_data:
    if iCalLib.HasTag(item,iCalLib.eTag.Begin):
      data_source = [None,None,None] # eDataIndexと合わせる
    elif iCalLib.HasTag(item,iCalLib.eTag.End):
      data_sources.append( data_source )
      data_source = None
    elif iCalLib.HasTag(item,iCalLib.eTag.DateStart):
      data_source[eDataIndex.Date] = datetime.strptime( iCalLib.GetTagValue(item), '%Y%m%d' )
    elif iCalLib.HasTag(item,iCalLib.eTag.Summary):
      data_source[eDataIndex.Name] = iCalLib.GetTagValue( item )
    elif iCalLib.HasTag(item,iCalLib.eTag.Description):
      data_source[eDataIndex.Options] = iCalLib.GetTagValue( item )

  release_title_data_list = []
  for data_source in data_sources:
    # @todo 日付の範囲
    release_title_data_list.append(
      ReleaseTitleData.Data(
        data_source[eDataIndex.Date]
        , data_source[eDataIndex.Name]
        , data_source[eDataIndex.Options]
      )
    )

  return release_title_data_list
