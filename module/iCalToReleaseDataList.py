#
# iCalendarからリリースデータのリストに変換
#
import urllib.request
from .lib import ReleaseDataListCreater
from .lib import Lib


# URLから作成
def WithURL( url, date_start_str, date_end_str ):
    file_data = urllib.request.urlopen( url )
    if file_data is None:
        return None

    ical_lines = []
    lines = file_data.readlines()
    for line in lines:
        ical_lines.append( line.decode().strip() ) # @memo stripで改行とか消してた

    return ReleaseDataListCreater.Create( ical_lines, Lib.StrToDate(date_start_str), Lib.StrToDate(date_end_str) )

# ファイルから作成
def WithFile( file_path, date_start_str, date_end_str ):
    file_data = open( file_path, mode='r', encoding='utf-8' )
    if file_data is None:
        return None

    ical_lines = []
    lines = file_data.readlines()
    for line in lines:
        ical_lines.append( line.strip() ) # @memo stripで改行とか消してた
    file_data.close()

    return ReleaseDataListCreater.Create( ical_lines, Lib.StrToDate(date_start_str), Lib.StrToDate(date_end_str) )
