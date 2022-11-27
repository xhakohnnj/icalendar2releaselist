#
# リリースデータリストから出力
#
from .lib import Lib


#
# ファイルに出力
#
def File( output_file, release_list, gamepass_in_list, gamepass_out_list ):
  def WriteFile( str ):
    output_file.write( str + '\n' )
    print( str )

  WriteFile( 'テンプレ 1' )
  WriteFile( '----------' )
  WriteFile( '【Xbox リリース スケジュール】' )
  WriteFile( '☆: Xbox Seres X|S 最適化　●: アップグレード対応　◇: ゲームパス対応' )
  WriteFile( '' )
  Lib.ForeachReleaseDataListConvTennpureFormat( release_list, lambda item: WriteFile( item ) )
  WriteFile( '' )
  WriteFile( '' )
  WriteFile( '' )
  WriteFile( 'テンプレ 2' )
  WriteFile( '----------' )
  WriteFile( '【XBOXゲームスペシャル】' )
  WriteFile( 'ttps://www.microsoft.com/ja-jp/store/deals/games/xbox' )
  WriteFile( '' )
  WriteFile( '【ゲームパス & EAPlay】' )
  WriteFile( '≪IN≫' )
  Lib.ForeachReleaseDataListConvTennpureFormat( gamepass_in_list, lambda item: WriteFile( item ) )
  WriteFile( '' )
  WriteFile( '≪OUT≫' )
  Lib.ForeachReleaseDataListConvTennpureFormat( gamepass_out_list, lambda item: WriteFile( item ) )
