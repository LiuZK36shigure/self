import csv
import re
from html.parser import HTMLParser

# 创建一个HTML解析器类
class HTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.teachers = []  # 存储教师信息
        self.teacher = [None]*4 #存储单个老师信息
        self.data_flag_iden = False
        self.data_flag_name = False

    def handle_starttag(self, tag, attrs):
        if tag == 'img':
            for attr in attrs:
                if attr[0] == 'src':
                    photo_path = attr[1]
                    self.teacher[0] = photo_path

                    pattern = r'/(\w+)-'
                    result = re.findall(pattern, photo_path)
                    if result:
                        self.teacher[1] = result[0]

        if tag == 'span':
            for attr in attrs:
                if attr[0] == 'class' and 'iden' in attr[1].split():
                    self.data_flag_iden = True
                if attr[0] == 'class' and 'name' in attr[1].split():
                    self.data_flag_name = True


    def handle_endtag(self, tag):
        if tag == 'span':
            if self.data_flag_iden or self.data_flag_name:
                self.data_flag_name = False
                self.data_flag_iden = False

    def handle_data(self, data):
        if self.data_flag_name:
            self.teacher[2] = data.strip()

        if self.data_flag_iden:
            self.teacher[3] = data.strip()

            if self.teacher[0] and self.teacher[1] and self.teacher[2] and self.teacher[3]:
                self.teachers.append(self.teacher.copy())
                self.teacher = [None] * 4

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
            department = teacher[3]
            name = teacher[2]
            title = teacher[1]
            photo_path = teacher[0]
            writer.writerow([department, name, title, photo_path])

# 示例用法
html_file_path1 = r"教授-数字媒体与设计艺术学院.htm"
html_file_path2 = (r"副教授-数字媒体与设计艺术学院.html")
html_file_path3 = (r"讲师-数字媒体与设计艺术学院.htm")# HTML文件路径
csv_file_path = r"teachers.csv"  # 保存CSV文件的路径

teachers = parse_html_file(html_file_path1) +parse_html_file(html_file_path2)+parse_html_file(html_file_path3)
save_teachers_to_csv(teachers, csv_file_path)