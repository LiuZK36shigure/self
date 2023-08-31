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
    with open(file_path, "r", encoding="utf-8") as file:
        html_data = file.read()

    parser = HTMLParser()
    parser.feed(html_data)

    return parser.teachers


# 将教师信息保存为CSV文件
def save_teachers_to_csv(teachers, csv_file_path):
    with open(csv_file_path, mode='w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Department', 'Name', 'Title', 'Photo'])
    for teacher in teachers:
        department = teacher[0]
        name = teacher[1]
        title = teacher[2]
        photo_path = teacher[3]
        writer.writerow([department, name, title, photo_path])

# 示例用法
html_file_path = r"C:\Users\1\Desktop\作业1网页\教授-数字媒体与设计艺术学院.htm"  # HTML文件路径
csv_file_path = r"C:\Users\1\Desktop\teachers.csv"  # 保存CSV文件的路径

teachers = parse_html_file(html_file_path)
save_teachers_to_csv(teachers, csv_file_path)