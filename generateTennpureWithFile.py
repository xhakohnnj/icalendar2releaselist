#
# テンプレ出力
# 
import sys
from enum import IntEnum, auto
from module import iCalToReleaseDataList
from module.tennpure import ReleaseDataListTo as GenerateTennpureTo


# 引数
class Args(IntEnum):
    OUTPUT_FILE                 = 1         # 出力ファイル
    INPUT_FILE_RELEASE          = auto()    # 入力ファイル(発売日)
    INPUT_FILE_GAMEPASS_IN      = auto()    # 入力ファイル(ゲームパスIN)
    INPUT_FILE_GAMEPASS_OUT     = auto()    # 入力ファイル(ゲームパスOUT)
    TITLE_RELEASE_DATE_START    = auto()    # 発売タイトルの日付の範囲(開始)
    TITLE_RELEASE_DATE_END      = auto()    # 発売タイトルの日付の範囲(終了)
    GAME_PASS_DATE_START        = auto()    # ゲームパスの日付の範囲(開始)
    GAME_PASS_DATE_END          = auto()    # ゲームパスの日付の範囲(終了)

# リリースカレンダー
release_list = iCalToReleaseDataList.WithFile( sys.argv[Args.INPUT_FILE_RELEASE], sys.argv[Args.TITLE_RELEASE_DATE_START], sys.argv[Args.TITLE_RELEASE_DATE_END] )
# ゲームパス IN
gamepass_in_list = iCalToReleaseDataList.WithFile( sys.argv[Args.INPUT_FILE_GAMEPASS_IN], sys.argv[Args.GAME_PASS_DATE_START], sys.argv[Args.GAME_PASS_DATE_END] )
# ゲームパス OUT
gamepass_out_list = iCalToReleaseDataList.WithFile( sys.argv[Args.INPUT_FILE_GAMEPASS_OUT], sys.argv[Args.GAME_PASS_DATE_START], sys.argv[Args.GAME_PASS_DATE_END] )

# テンプレ出力
with open( sys.argv[Args.OUTPUT_FILE], mode='w', encoding='utf-8', newline='\n' ) as output_file:
    GenerateTennpureTo.File( output_file, release_list, gamepass_in_list, gamepass_out_list )
