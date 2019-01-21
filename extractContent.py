import matplotlib.pyplot as plt
from bs4 import BeautifulSoup, Comment

"""
函数功能：用于自动识别并提取招标公告的正文信息
输入：参数一 html_str HTML格式的字符串
      参数二 max_step 用于控制获取的内容精度，默认值是10，一般不需要设置
输出：返回值 字符串形式的div
"""

def extractContent(html_str, max_step=10):
    dom_tree = BeautifulSoup(html_str, "html.parser")
    [s.extract() for s in dom_tree({'script', 'h1'})]
    for element in dom_tree(text=lambda text: isinstance(text, Comment)):
        element.extract()
    node_list = dom_tree.find_all({'p', 'span'})
    max = 0
    max_p_index = 0
    for index in range(len(node_list)):
        if len(node_list[index].text) > max:
            max_p_index = index
            max = len(node_list[index].text)
    node_point = node_list[max_p_index]
    step = 1
    while node_point is not None and node_point.parent is not None and len(node_point.text.replace('\n', '')) != len(
            node_point.parent.text.replace('\n', '')):
        node_point = node_point.parent
        step = step + 1
        if step >= max_step:
            break
    return str(node_point)
