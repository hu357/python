字符串切片
>>> str1 = 'I love fishC'
>>> str1[:6]
'I love'
索引字符
>>> str1[5]
'e'
插入字符串
>>> str1[:6] + '插入的字符串' + str1[6:]
'I love插入的字符串 fishC'
numeric包括全进制，罗马，中文字符
digit包括全进制，罗马数字，不包括中文
numeric也不包括byte数字，会报错
>>> str7 = 'sssssssaaaaassssss'
>>> str7.translate(str.maketrans('s','b'))
'bbbbbbbaaaaabbbbbb'
>>> str.maketrans('s','b')
{115: 98}#'s','b'的ASCII码值
