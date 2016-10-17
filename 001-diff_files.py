# coding:utf-8
'''
比较两个分件内容，类似于git，仅适用于在linux上使用
'''
import subprocess


def diff_files(filename1, filename2):
    pipeline = ['diff -U 3 %(filename1)s %(filename2)s'
                % {'filename1': filename1, 'filename2': filename2}]

    if subprocess.call(['which', 'colordiff']) == 0:
        pipeline.append('colordiff')

    pipeline.append('less -R')

    cmd = ' | '.join(pipeline)
    subprocess.check_call(cmd, shell=True)
