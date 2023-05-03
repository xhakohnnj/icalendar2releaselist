#
# データの定義
#
# たぶんそんなに量は無いのでとりあえずここでまとめておく.
#


# リリースデータ
class ReleaseData:
    def __init__( self, date=None, title=None, options=None, useTime=False ):
      self.date = date        # リリース日
      self.title = title      # タイトル名
      self.options = options  # オプション
      self.useTime = useTime  # 時間を使用
