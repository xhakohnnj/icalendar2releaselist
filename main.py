from module import UrlToDataList


url = "https://calendar.google.com/calendar/ical/i3h9mf13qmbe2qq927gaadagfg%40group.calendar.google.com/public/basic.ics"

data_list = UrlToDataList.Main( url )
for data in data_list:
  print( '{0}　{1}　{2}'.format( data.date.strftime('%m/%d'), data.title, data.options ) )
