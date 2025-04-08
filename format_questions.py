from docx import Document
from docx.shared import Pt
from docx.enum.text import WD_LINE_SPACING, WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import re

def format_questions(input_file, output_file):
    # 打开文档
    doc = Document(input_file)
    
    # 设置默认字体为微软雅黑
    style = doc.styles['Normal']
    style.font.name = '微软雅黑'
    style._element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')
    style.font.size = Pt(10.5)  # 五号字体大小约为10.5磅
    
    # 定义选项的正则表达式模式（支持更多的选项格式）
    option_pattern = re.compile(r'^[A-D][.、)）．:：]')
    
    # 处理每个段落
    for paragraph in doc.paragraphs:
        # 设置1.3倍行距
        paragraph.paragraph_format.line_spacing_rule = WD_LINE_SPACING.MULTIPLE
        paragraph.paragraph_format.line_spacing = 1.3
        
        # 完全清除所有缩进设置
        paragraph.paragraph_format.first_line_indent = Pt(0)
        paragraph.paragraph_format.left_indent = Pt(0)
        
        # 确保有段落属性
        if paragraph._p.pPr is None:
            paragraph._p.get_or_add_pPr()
        
        # 移除所有与缩进相关的XML属性
        if paragraph._p.pPr.ind is not None:
            paragraph._p.pPr.remove(paragraph._p.pPr.ind)
        
        # 取消"定义文档网格时对齐网格"选项
        snap_to_grid = OxmlElement('w:snapToGrid')
        snap_to_grid.set(qn('w:val'), '0')
        
        # 检查是否已存在snapToGrid元素
        existing_snap = paragraph._p.pPr.find(qn('w:snapToGrid'))
        if existing_snap is not None:
            # 如果存在，则更新值为0
            existing_snap.set(qn('w:val'), '0')
        else:
            # 如果不存在，则添加新元素
            paragraph._p.pPr.append(snap_to_grid)
        
        # 检查是否是选项
        text = paragraph.text.strip()
        if option_pattern.match(text):
            # 选项左对齐
            paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT
            # 选项不加粗
            for run in paragraph.runs:
                run.font.bold = False
                run.font.name = '微软雅黑'
                run._element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')
                # 移除所有加粗属性
                if run._element.rPr is not None:
                    for b_element in run._element.rPr.findall('.//w:b', {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}):
                        run._element.rPr.remove(b_element)
                    for b_element in run._element.rPr.findall('.//w:bCs', {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}):
                        run._element.rPr.remove(b_element)
        else:
            # 题干加粗
            for run in paragraph.runs:
                run.font.bold = True
                run.font.name = '微软雅黑'
                run._element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')
                # 确保中文也加粗
                if run._element.rPr is not None:
                    if 'b' not in run._element.rPr.attrib:
                        run._element.rPr.set('b', '1')
                    if 'bCs' not in run._element.rPr.attrib:
                        run._element.rPr.set('bCs', '1')
    
    # 保存修改后的文档
    doc.save(output_file)

if __name__ == '__main__':
    input_file = 'input.docx'  # 输入文件路径
    output_file = 'output.docx'  # 输出文件路径
    format_questions(input_file, output_file)