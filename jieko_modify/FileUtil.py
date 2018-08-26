import configparser
import os

import time

import xlrd
from xlutils.copy import copy




class FileUtile:
    def __init__(self,path):
        self.filepath=path
    def getTime(self):
        return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    def read_excel(self,x,y):
        workbook=xlrd.open_workbook(self.filepath)
        sheet=workbook.sheet_by_index(0)
        aa=sheet.cell(x,y).value
        return aa
    def read_excel_h_w(self):
        workbook=xlrd.open_workbook(self.filepath)
        sheet=workbook.sheet_by_index(0)
        return [sheet.nrows,sheet.ncols]
    def write_excel(self,x,y,str):
        workbook=xlrd.open_workbook(self.filepath)
        workbooknew=copy(workbook)
        ws=workbooknew.get_sheet(0)
        ws.write(x,y,str)
        workbooknew.save(self.filepath)

