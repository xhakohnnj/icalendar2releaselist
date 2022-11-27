#
# テンプレ関係のライブラリ
#


#
# データリストをテンプレのフォーマットに変換して各アイテムごとにコールバックを呼び出す.
#
# date_list   データリスト
# func        データ1つに行う処理
#
def ForeachReleaseDataListConvTennpureFormat( release_data_list, func, *args ):
  year_tmp = None
  output_year = False
  insert_newline = False

  for data in release_data_list:
    if year_tmp is None:
      year_tmp = data.date.year

    # 年をまたいだら年も出力する.
    if year_tmp is None or not year_tmp is None and year_tmp != data.date.year:
      year_tmp = data.date.year
      output_year = True
      insert_newline = True

    date = None
    if output_year is True:
      date = data.date.strftime('%Y/%m/%d')
    else:
      date = data.date.strftime('%m/%d')
    item = '{0}　{1}'.format( date, data.title )

    # 改行を頭に.
    if insert_newline is True:
      item = '\n' + item
      insert_newline = False

    if not data.options == None and 0 < len(data.options): # なんかNoneじゃなくて空白も入ってるところもあるのでlenでもチェック.
      item += ' {0}'.format( data.options )
    func( item )
