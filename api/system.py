#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Author: 潘高
LastEditors: 潘高
Date: 2023-03-26 19:13:01
LastEditTime: 2023-04-03 19:27:20
Description: 系统类
usage: 调用window.pywebview.api.<methodname>(<parameters>)从Javascript执行
'''

import json
import os
import platform
import subprocess

import webview

from pyapp.config.config import Config
from pyapp.update.update import AppUpdate


class System:
    '''系统类'''

    window = None

    def py2js(self, func, info):
        '''调用js中挂载到window的函数'''
        infoJson = json.dumps(info)
        System.window.evaluate_js(f"{func}('{infoJson}')")

    def pyCreateFileDialog(self, fileTypes=['全部文件 (*.*)'], directory=''):
        '''打开文件对话框'''
        # 可选文件类型
        # fileTypes = ['Excel表格 (*.xlsx;*.xls)']
        fileTypes = tuple(fileTypes)    # 要求必须是元组
        result = System.window.create_file_dialog(dialog_type=webview.OPEN_DIALOG, directory=directory, allow_multiple=True, file_types=fileTypes)
        resList = list()
        if result is not None:
            for res in result:
                filePathList = os.path.split(res)
                dir = filePathList[0]
                filename = filePathList[1]
                ext = os.path.splitext(res)[-1]
                resList.append({
                    'filename': filename,
                    'ext': ext,
                    'dir': dir,
                    'path': res
                })
        return resList

    def system_getAppInfo(self):
        '''程序基础配置信息'''
        return {
            'appName': Config.appName,  # 应用名称
            'appVersion': Config.appVersion  # 应用版本号
        }

    def system_checkNewVersion(self):
        '''检查更新'''
        appUpdate = AppUpdate()    # 程序更新类
        res = appUpdate.check()
        return res

    def system_downloadNewVersion(self):
        '''下载新版本'''
        appUpdate = AppUpdate()    # 程序更新类
        res = appUpdate.run()
        return res

    def system_cancelDownloadNewVersion(self):
        '''取消下载新版本'''
        appUpdate = AppUpdate()    # 程序更新类
        res = appUpdate.cancel()
        return res

    def system_pyOpenFile(self, path):
        '''用电脑默认软件打开本地文件'''
        systemType = platform.platform()    # 获取系统类型
        # 判断以下当前系统类型
        if 'mac' in systemType:
            path = path.replace("\\", "/")
            print('path', path)
            subprocess.call(["open", path])
        else:
            path = path.replace("/", "\\")
            os.startfile(path)
