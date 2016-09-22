'''
dir = tools/db/schema_diff.py
------------------------------------------------------------------------------
subprocess()
subprocess(子进程)  开启一个子进程
语法实例:
subprocess.check_call(['mysqladmin', '-f', '-u', 'root', 'drop', name])
retcode = subprocess.call(["ls", "-l"])

subprocess.call()
父进程等待子进程完成后退出，成功返回0，失败非0
subprocess.check_call()
父进程等待子进程完成，返回0，检查returncode不为0则举出错误subprocess.CalledProcessError
成功返回0，失败非0
必须存在[]将命令括起来,错误实例：
retcode = subprocess.check_call("ls","-a")

---------------------------------------------------------------------------
endwith()
str.endwith() 字符串str的最后一个字符，如果匹配则返回true，不匹配返回fasle
举例：
if not db_url.endswith('/'):
        db_url += '/'

--------------------------------------------------------------------------
join() 在每个字符串中间都加添加
举例：
test="aa  bb  cc"
cmd='|'.join(test)
print cmd
a|a| | |b|b| | |c|c

--------------------------------------------------------------------------
'''
