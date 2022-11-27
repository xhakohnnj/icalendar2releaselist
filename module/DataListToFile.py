#
# リストからファイルに出力
#
# output_file     出力先のファイル
# date_list       リスト
#
def Main( output_file, data_list ):
  year_tmp = None
  output_year = False
  insert_newline = False

  for data in data_list:
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
    print( item )
    if not output_file is None:
      output_file.write( item + '\n' )
