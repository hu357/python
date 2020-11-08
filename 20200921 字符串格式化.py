>>> "{0} love {1}.{2}".format("I","fishC","com")
'I love fishC.com'
>>> "{a} love {b}.{c}".format(a="I",b="fishC",c="com")
'I love fishC.com'
>>> "{0} love {b}.{c}".format("I",b="fishC",c="com")
'I love fishC.com'
数字1 1f是保留小数点后一位
>>> "{{0}}".format("不打印")
'{0}'
>>> "{0:.1f}{1}".format(27.658,"GB")
'27.7GB'

>>> '%c' % 97
'a'
>>> '%c %c %c' % (97,98,99)#必须有括号
'a b c'
>>> '%s' % 'I love fishC.com'
'I love fishC.com'
>>> '%d + %d =  %d' % (4,5,4+5)
'4 + 5 =  9'

