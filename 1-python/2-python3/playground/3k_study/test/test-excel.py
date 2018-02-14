#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import xlrd  # 导入读模块
import xlwt  # 导入写模块


def read_from_excel():
    # 打开Excel文件读取数据
    workbook = xlrd.open_workbook('test.xls')

    # 获取所有工作表名（列表）
    sheet = workbook.sheet_names()
    print(sheet)
    print(type(sheet))

    # 获取一个工作表
    sheet1 = workbook.sheets()[0]
    sheet2 = workbook.sheet_by_index(1)
    sheet3 = workbook.sheet_by_name('告警总览')
    print(sheet1.name)
    print(sheet2.name)
    print(sheet3.name)

    # 获取整行和整列的值（数组）
    print(sheet2.row_values(0))
    print(sheet2.col_values(0))

    # 获取行数和列数
    nrows = sheet2.nrows
    ncols = sheet2.ncols
    print(nrows, ncols)

    # 循环打印每行的值
    for i in range(nrows):
        print(sheet2.row_values(i))

    # 获取单元格内容 （使用单元格坐标）
    cell_A1 = sheet2.cell(0, 0).value
    cell_C2 = sheet2.cell(1, 2).value
    print(cell_A1, cell_C2)

    # 获取单元格内容（使用行列索引）
    cell_A1 = sheet2.row(0)[0].value
    cell_C2 = sheet2.col(2)[1].value
    print(cell_A1, cell_C2)


def create_excel():
    # 创建工作簿
    f = xlwt.Workbook()

    # 创建工作表
    sheet1 = f.add_sheet(u'告警总览', cell_overwrite_ok=True)  # 创建sheet
    sheet2 = f.add_sheet(u'告警明细', cell_overwrite_ok=True)  # 创建sheet

    # 定义表头格式
    head_title = ['区域', '站名', '告警网元', '告警产生时间', '告警消除时间', '告警id', '告警明细', '告警诊断信息', '告警分类(业务)', '告警明细分类', '告警解释']

    # 生成第一行
    for i in range(0, len(head_title)):
        sheet2.write(0, i, head_title[i])
        i + 1

    # 保存文件
    f.save('t.xls')
