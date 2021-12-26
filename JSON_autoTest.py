import json
with open ('JSON_response.txt', encoding = 'utf8') as f:
    templates = json.load(f)
def CheckInt(item):
    return isinstance(item, int)
def CheckStr(item):
    return isinstance(item, str)
def CheckBool(item):
    return isinstance(item, bool)
def CheckUrl(item):
    if isinstance(item, str):
        return item.startswith('http://') or item.startswith('https://')
    else:
        return False
def CheckStrValue(item, val):
    if isinstance(item,str):
        return item in val
    else:
        return False
def ErrorLog(item, value, string):
    Error.append({item: f'{value},{string}'})
ListOfItems = {'timestamp':'int', 'item_price':'int', 'referer':'url', 'location':'url', 'item_url':'url',
               'remoteHost':'str', 'partyId':'str','sessionId':'str','pageViewId':'str','item_id':'str',
               'basket_price':'str','userAgentName': 'str', 'eventType':'val', 'detectedDuplicate':'bool',
               'detectedCorruption':'bool','firstInSession':'bool'}
Error = []
for items in templates:
    for item in items:
        if item in ListOfItems:
            if ListOfItems[item]=='int':
                if not CheckInt(items[item]):
                    ErrorLog(item, items[item], f'ожидали тип {ListOfItems[item]}')
            elif ListOfItems[item]== 'str':
                if not CheckStr(items[item]):
                    ErrorLog(item, items[item], f'ожидали тип {ListOfItems[item]}')
            elif ListOfItems[item]== 'bool':
                if not CheckBool(items[item]):
                    ErrorLog(item, items[item], f'ожидали тип {ListOfItems[item]}')
            elif ListOfItems[item]== 'url':
                if not CheckUrl(items[item]):
                    ErrorLog(item, items[item], f'ожидали тип {ListOfItems[item]}')
            elif ListOfItems[item]== 'val':
                if not CheckStrValue(items[item], ['itemBuyEvent','itemViewEvent']):
                    ErrorLog(item, items[item], f'ожидали значение itemBuyEvent или itemViewEvent')
            else:
                ErrorLog(item, items[item], 'неожиданное значение')
        else:
            ErrorLog(item, items[item], 'неожиданная переменная')
if Error == []:
    print('pass')
else:
    print('Fail')
    print(Error)