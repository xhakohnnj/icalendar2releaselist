#
# データの定義
#
# たぶんそんなに量は無いのでとりあえずここでまとめておく.
#


# リリースデータ
class ReleaseData:
    def __init__( self, date=None, title=None, options=None ):
      self.date = date        # リリース日
      self.title = title      # タイトル名
      self.options = options  # オプション
