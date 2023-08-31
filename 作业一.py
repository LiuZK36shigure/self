import re
import csv
from html.parser import HTMLParser

# 创建一个HTML解析器类
class HTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.teachers = []  # 存储教师信息
        self.teacher = {}  # 存储当前解析的教师信息


# 解析HTML文件
def parse_html_file(file_path):

# 将教师信息保存为CSV文件
def save_teachers_to_csv(teachers, csv_file_path):


# 示例用法
html_file_path = r"C:\Users\1\Desktop\作业1网页\教授-数字媒体与设计艺术学院.htm"  # HTML文件路径
csv_file_path = r"C:\Users\1\Desktop\teachers.csv"  # 保存CSV文件的路径

