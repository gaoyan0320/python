import ConfigParser

conf=ConfigParser.ConfigParser()
conf.read('example.conf')
print conf.get('db1',"conn_str")
print conf.get('db2',"conn_str")