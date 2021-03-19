__author__ = 'Ram Anandh'
__email__ = "rsramanandh@gmail.com"
__credits__ = ["rsramanandh@gmail.com"]

from datetime import datetime
import os
from mss import mss


class Reports:
    def __init__(self, testcase_name, path_base,
                 take_screenshot_on_fail=True, take_screenshot_on_pass=False,
                 stop_testcase_on_fail=False):
        self.path_base = path_base
        self.take_screenshot_on_fail = take_screenshot_on_fail
        self.stop_testcase_on_fail = stop_testcase_on_fail
        self.take_screenshot_on_pass = take_screenshot_on_pass

        self.testcase_name = testcase_name
        self.html_filename = self.testcase_name + '_' + str(
            datetime.now().strftime("%m%d%Y_%H%M%S")) + '.html'
        self.file_name = None

    def info(self, info_string):
        self.write_to_html(text=info_string, result_type='info')

    def report(self, condition, info_pass="", info_fail="", testcase=None):
        text = info_pass if condition else info_fail
        if condition:
            self.write_to_html(text=text, testcase=testcase, result_type='pass')

        else:
            ss_filename = (self.testcase_name + str(
                datetime.now().strftime("%m%d%Y_%H%M%S")) + '.jpg').replace(" ", "_")
            self.take_screenshot(ss_filename=ss_filename)
            self.write_to_html(text=text, testcase=testcase, result_type='fail')

    def error(self, text, testcase=None):
        self.write_to_html(text=text, result_type="error", testcase=testcase)

    def warning(self, text):
        self.write_to_html(text=text, result_type="fail")

    def take_screenshot(self, ss_filename):
        ss_file_path = os.path.abspath(
            os.path.join(self.path_base, "logs", "screenshots", ss_filename))
        with mss() as sct:
            sct.shot(output=ss_file_path)
        self.add_image_to_html(ss_file_path)

    def create_file(self):
        self.file_name = os.path.join(os.getcwd(), 'logs', self.html_filename)
        file_object = open(self.file_name, "w+")
        style_sheet_1 = (os.path.join(os.getcwd(), 'logs', 'assets', 'stylesheet_1.css'))
        header_css = (os.path.join(os.getcwd(), 'logs', 'assets', 'header_stylesheet.css'))
        html_template = f'<!DOCTYPE html><html><head><meta charset="utf-8">' \
                        '<meta http-equiv="X-UA-Compatible" content="IE=edge">	' \
                        '<meta name="viewport" content="width=device-width, initial-scale=1">' \
                        f'<title>{self.testcase_name}</title>' \
                        f'<link rel="stylesheet" href="{style_sheet_1}">' \
                        f'<link rel="stylesheet" href="{header_css}">' \
                        '<link href="http://fonts.googleapis.com/css?family=Cookie" ' \
                        'rel="stylesheet" type="text/css">' \
                        '</head><body><header class="header-fixed">	' \
                        f'<div class="header-limiter"><h1>{self.testcase_name}</h1>' \
                        '</div></header><div class="header-fixed-placeholder"></div>' \
                        '<!-- The content of your page would go here. -->'
        file_object.write(html_template)

    def finish_report(self):
        self.write_to_html(text="This is the last step in testcase.", result_type='info-lite')
        file_object = open(self.file_name, 'a+')
        html_content = '<script ' \
                       'src="http://ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js">' \
                       '</script>' \
                       '<script>$(document).ready(function(){' \
                       'var showHeaderAt = 150;var win = $(window),body = $("body");' \
                       'if(win.width() > 600){	win.on("scroll", function(e){' \
                       'if(win.scrollTop() > showHeaderAt) {body.addClass("fixed");}' \
                       'else {body.removeClass("fixed");}});}});</script></body></html>'
        file_object.write(html_content)

    def write_to_html(self, text, testcase=None, result_type="info"):
        file_object = open(self.file_name, 'a+')
        color = 'black'
        font_style = 'normal'
        if result_type == 'pass':
            font_style, color = 'normal', 'green'
        elif result_type == 'fail':
            font_style, color = 'normal', '#BDB76B'
        elif result_type == 'error':
            font_style, color = 'normal', 'red'
        elif result_type == 'info':
            font_style, color = 'bold', 'black'
        elif result_type=="info-lite":
            font_style, color = 'normal', 'black'
        text_style = f"font: {font_style} 20px/1.5 'Open Sans', sans-serif; color:{color}"
        date_time_style = "font: bold 20px/1.5 'Open Sans', sans-serif; color:blue"
        date_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        testcase = testcase if testcase else ""
        html_content = f'<div style="display: flex;">' \
                       f'<div style="{date_time_style}">{date_time}&nbsp;{result_type}&nbsp;' \
                       f'</div> <div style="{text_style}">{testcase}&nbsp;{text}</div></div>'
        file_object.write(html_content)

    def add_image_to_html(self, image_path):
        """Method to add the screenshot to html report"""
        file_object = open(self.file_name, 'a+')
        html_content = f'<div><img src={image_path} width="500" height="300"></div>'
        file_object.write(html_content)
