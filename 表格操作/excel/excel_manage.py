# -*- coding:utf-8 -*-
"""
 excel 相关处理
"""
import xlrd


class excel_manange():
    # 打开excel
    def open_excel(self, file_name):
        data = xlrd.open_workbook(file_name)
        return data

    # 根据index获取sheet
    def get_sheet_by_index(self, data, sheet_index):
        sheet = data.sheet_by_index(sheet_index)
        return sheet

    # 根据name获取sheet
    def get_sheet_by_name(self, data, sheet_name):
        sheet = data.sheet_by_name(sheet_name)
        return sheet

    # 获取整行的数据
    def get_row_values(self, sheet, row_num):
        data = sheet.row_values(row_num)
        return data

    # 获取整列的数据
    def get_col_values(self, table, col_num):
        data = table.col_values(col_num)
        return data

    # 获取行数
    def get_row_num(self, table):
        row_num = table.nrows
        return row_num

    # 获取列数
    def get_col_num(self, table):
        col_num = table.ncols
        return col_num

    # 获取某个单元的数据
    def get_cell_data(self, table, row, col):
        cell = table.cell(row, col).value
        return cell

    # 设置数据
    # 类型 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
    def set_cell(self, table, row, col, ctype, value, xf):
        table.put_cell(row, col, ctype, value, xf)

    def write_data(self, sheet, row, col, value):
        sheet.write(row, col, value)
