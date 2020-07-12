'''
输出路径自动建立，
建立规则：文件名为分割之后的文件个数（比如：自动建立文件夹36_sheet,表示将原始表格分割成36个子表）
'''
import pandas as pd
import math
import os


class SegSheet():
    def __init__(self,input_path,rows_every_sheet):
        self.input_path = input_path
        self.rows_every_sheet = rows_every_sheet

    def read_csv_or_xlsx_xls(self):
        format = self.input_path.split('.')[-1]
        if format =='xlsx' or format == 'xls':
            df_1 = pd.read_excel(self.input_path, dtype=object)
        elif format == 'csv':
            df_1 = pd.read_csv(self.input_path)
        # print(df_1)
        return df_1

    def floor_seg_sheet(self):
        '''eg:将含3523行的表格拆成35个表，前边每个表有100行有效数据，最后一个表含有123行有效数据。'''
        df_1 = self.read_csv_or_xlsx_xls()
        num = math.floor(len(df_1)/self.rows_every_sheet)   #num表示几个文件
        output_path = '.\\'+str(num)+'_sheet'          # './'+str(num)+'_sheets'
        print(output_path)
        print(num)
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        else:
            for file in os.listdir(output_path):
                file_path = os.path.join(output_path,file)
                print(os.path.join(output_path, file))
                os.remove(file_path)
        for i in range(num):
            if i < num-1:
                start_index = i*self.rows_every_sheet
                end_index = (i+1)*self.rows_every_sheet
                df_2 = df_1[start_index:end_index]
                df_2.to_excel(output_path+'/'+str(i+1)+'.xlsx', index=False)
            else:
                df_3 = df_1[(num-1)*self.rows_every_sheet:]
                df_3.to_excel(output_path+'/'+str(i+1)+'.xlsx', index=False)

    def ceil_seg_sheet(self):
        '''eg:将含3523行的表格拆成36个表，前边每个表有100行有效数据，最后一个表含有23行有效数据。'''
        df_1 = self.read_csv_or_xlsx_xls()
        num = math.ceil(len(df_1) / self.rows_every_sheet)  # num表示几个文件
        output_path = '.\\' + str(num) + '_sheet'  # './'+str(num)+'_sheets'
        print(output_path)
        print(num)
        if not os.path.exists(output_path):
            os.makedirs(output_path)
        else:
            for file in os.listdir(output_path):
                file_path = os.path.join(output_path, file)
                print(os.path.join(output_path, file))
                os.remove(file_path)
        for i in range(num):
            start_index = i * self.rows_every_sheet
            end_index = min((i + 1) * self.rows_every_sheet,len(df_1))
            df_2 = df_1[start_index:end_index]
            df_2.to_excel(output_path + '/' + str(i + 1) + '.xlsx', index=False)

input_path = './BC_lack.xlsx'
rows_every_sheet = 100  # 每个子表的行数
seg_sheet = SegSheet(input_path,rows_every_sheet)
seg_sheet.ceil_seg_sheet()