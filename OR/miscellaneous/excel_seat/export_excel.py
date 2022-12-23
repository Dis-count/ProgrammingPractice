import xlwt
import easygui as g
from GenerateLocation import Table as table


def setUnitStyle(name, height, bold=False):
    style = xlwt.XFStyle()

    font = xlwt.Font()
    font.name = name
    font.bold = bold
    font.color_index = 4
    font.height = height
    style.font = font

    return style


def createExcel():
    #創建工作簿
    e = xlwt.Workbook()

    #創建表格sheet1
    sheet1 = e.add_sheet(u'sheet1', cell_overwrite_ok=True)

    #創建第一行
    sheet1.write_merge(0, 0, 0, 3, u'', setUnitStyle(
        'Times New Roman', 500, False))
    sheet1.write_merge(0, 0, 3, 10, u'ACM 404集训座位表',
                       setUnitStyle('Times New Roman', 500, False))
    sheet1.write_merge(1, 1, 1, 4, u'', setUnitStyle(
        'Times New Roman', 300, False))
    sheet1.write_merge(1, 1, 6, 10, u'', setUnitStyle(
        'Times New Roman', 300, False))
    sheet1.write(1, 5, u'讲台', setUnitStyle(u'微软雅黑', 400, True))
    sheet1.write_merge(3, 5, 5, 6, u'走廊', setUnitStyle(
        'Times New Roman', 800, False))
    sheet1.write_merge(2, 2, 5, 6, u'', setUnitStyle(
        'Times New Roman', 300, False))
    sheet1.write_merge(6, 6, 5, 6, u'', setUnitStyle(
        'Times New Roman', 300, False))
    sheet1.write(1, 0, u'门', setUnitStyle(u'微软雅黑', 400, False))
    gt = table()
    t = gt.getTable()

    for i in range(5):
        for j in range(9):
            if t[i][j] == 0:
                continue
            temp = j
            if temp >= 5:
                temp += 2
            sheet1.write(i+2, temp, t[i][j], setUnitStyle(u'微软雅黑', 250, False))
    filename = '404座位表.xls'
    e.save(filename)  # 坑,xlsx无法打开

    remind = g.msgbox(msg=filename + ' 已生成！', title='404座位表生成器',
                      ok_button='取消')


if __name__ == '__main__':
    createExcel()
