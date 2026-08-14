import os
import docx
from docx import Document
from docx.shared import Inches, Pt, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls

def create_document():
    doc = Document()
    
    # ----------------------------------------------------
    # Page Setup (Margins)
    # ----------------------------------------------------
    sections = doc.sections
    for section in sections:
        section.top_margin = Inches(1)
        section.bottom_margin = Inches(1)
        section.left_margin = Inches(1)
        section.right_margin = Inches(1)

    # ----------------------------------------------------
    # Styling Helpers
    # ----------------------------------------------------
    PRIMARY_COLOR = RGBColor(31, 78, 121)    # Deep Navy (#1F4E79)
    SECONDARY_COLOR = RGBColor(89, 89, 89)   # Slate Grey (#595959)
    TEXT_COLOR = RGBColor(38, 38, 38)        # Off-Black (#262626)
    ACCENT_COLOR = RGBColor(0, 128, 128)     # Teal (#008080)
    BG_LIGHT_HEX = "F2F4F7"
    BORDER_GRAY_HEX = "D3D3D3"
    
    FONT_NAME = 'TH Sarabun PSK'
    FONT_CODE = 'Consolas'

    def set_font_run(run, font_name=FONT_NAME, size_pt=16, bold=False, italic=False, color=TEXT_COLOR):
        run.font.name = font_name
        run.font.size = Pt(size_pt)
        run.bold = bold
        run.italic = italic
        run.font.color.rgb = color
        
        # Set fonts for Complex Script (Thai) and East Asia
        rPr = run._r.get_or_add_rPr()
        rFonts = OxmlElement('w:rFonts')
        rFonts.set(qn('w:ascii'), font_name)
        rFonts.set(qn('w:hAnsi'), font_name)
        rFonts.set(qn('w:eastAsia'), font_name)
        rFonts.set(qn('w:cs'), font_name)
        rPr.append(rFonts)

    def add_styled_paragraph(text="", style_name='Normal', align=WD_ALIGN_PARAGRAPH.LEFT, space_before=0, space_after=6, line_spacing=1.15):
        p = doc.add_paragraph()
        p.alignment = align
        p_format = p.paragraph_format
        p_format.space_before = Pt(space_before)
        p_format.space_after = Pt(space_after)
        p_format.line_spacing = line_spacing
        
        if text:
            run = p.add_run(text)
            set_font_run(run)
        return p

    def add_heading_1(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(6)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        set_font_run(run, FONT_NAME, 20, bold=True, color=PRIMARY_COLOR)
        return p

    def add_heading_2(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(10)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        set_font_run(run, FONT_NAME, 18, bold=True, color=ACCENT_COLOR)
        return p

    def add_heading_3(text):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(8)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.keep_with_next = True
        run = p.add_run(text)
        set_font_run(run, FONT_NAME, 16, bold=True, color=SECONDARY_COLOR)
        return p

    def add_bullet_point(text, level=0):
        p = doc.add_paragraph()
        p.paragraph_format.space_before = Pt(0)
        p.paragraph_format.space_after = Pt(3)
        p.paragraph_format.left_indent = Inches(0.25 * (level + 1))
        
        bullet_char = "•  " if level == 0 else "⁃  "
        run_bullet = p.add_run(bullet_char)
        set_font_run(run_bullet, FONT_NAME, 16, bold=True, color=ACCENT_COLOR)
        
        run_text = p.add_run(text)
        set_font_run(run_text, FONT_NAME, 16, color=TEXT_COLOR)
        return p

    def add_formula_box(equation_str, desc_lines=None):
        table = doc.add_table(rows=1, cols=1)
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        table.autofit = False
        
        cell = table.cell(0, 0)
        cell.width = Inches(5.5)
        
        # Set shading and border
        shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{BG_LIGHT_HEX}"/>')
        cell._tc.get_or_add_tcPr().append(shading)
        
        tcBorders = parse_xml(f'''
            <w:tcBorders {nsdecls("w")}>
                <w:top w:val="single" w:sz="6" w:space="0" w:color="{BORDER_GRAY_HEX}"/>
                <w:left w:val="single" w:sz="18" w:space="0" w:color="1F4E79"/>
                <w:bottom w:val="single" w:sz="6" w:space="0" w:color="{BORDER_GRAY_HEX}"/>
                <w:right w:val="single" w:sz="6" w:space="0" w:color="{BORDER_GRAY_HEX}"/>
            </w:tcBorders>
        ''')
        cell._tc.get_or_add_tcPr().append(tcBorders)
        
        p = cell.paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(6)
        
        run_eq = p.add_run(equation_str)
        set_font_run(run_eq, FONT_NAME, 16, bold=True, color=PRIMARY_COLOR)
        
        if desc_lines:
            for desc in desc_lines:
                p_desc = cell.add_paragraph()
                p_desc.paragraph_format.space_before = Pt(2)
                p_desc.paragraph_format.space_after = Pt(2)
                p_desc.paragraph_format.left_indent = Inches(0.25)
                run_desc = p_desc.add_run(desc)
                set_font_run(run_desc, FONT_NAME, 14, color=SECONDARY_COLOR)

    def add_code_block(code_text):
        table = doc.add_table(rows=1, cols=1)
        table.alignment = WD_TABLE_ALIGNMENT.CENTER
        table.autofit = False
        
        cell = table.cell(0, 0)
        cell.width = Inches(5.5)
        
        shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="F9F9F9"/>')
        cell._tc.get_or_add_tcPr().append(shading)
        
        tcBorders = parse_xml(f'''
            <w:tcBorders {nsdecls("w")}>
                <w:top w:val="single" w:sz="4" w:space="0" w:color="{BORDER_GRAY_HEX}"/>
                <w:left w:val="single" w:sz="12" w:space="0" w:color="7F7F7F"/>
                <w:bottom w:val="single" w:sz="4" w:space="0" w:color="{BORDER_GRAY_HEX}"/>
                <w:right w:val="single" w:sz="4" w:space="0" w:color="{BORDER_GRAY_HEX}"/>
            </w:tcBorders>
        ''')
        cell._tc.get_or_add_tcPr().append(tcBorders)
        
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(4)
        p.paragraph_format.space_after = Pt(4)
        p.paragraph_format.line_spacing = 1.0
        
        run_code = p.add_run(code_text)
        set_font_run(run_code, FONT_CODE, 11, color=RGBColor(40, 40, 40))

    def style_table_header(row, bg_color_hex="1F4E79"):
        for cell in row.cells:
            shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{bg_color_hex}"/>')
            cell._tc.get_or_add_tcPr().append(shading)
            
            tcBorders = parse_xml(f'''
                <w:tcBorders {nsdecls("w")}>
                    <w:top w:val="single" w:sz="12" w:space="0" w:color="000000"/>
                    <w:bottom w:val="single" w:sz="12" w:space="0" w:color="000000"/>
                    <w:left w:val="none"/>
                    <w:right w:val="none"/>
                </w:tcBorders>
            ''')
            cell._tc.get_or_add_tcPr().append(tcBorders)

    def style_table_row(row, is_even=False):
        bg_color = "F9FBFD" if is_even else "FFFFFF"
        for cell in row.cells:
            shading = parse_xml(f'<w:shd {nsdecls("w")} w:fill="{bg_color}"/>')
            cell._tc.get_or_add_tcPr().append(shading)
            
            tcBorders = parse_xml(f'''
                <w:tcBorders {nsdecls("w")}>
                    <w:top w:val="none"/>
                    <w:bottom w:val="single" w:sz="4" w:space="0" w:color="{BORDER_GRAY_HEX}"/>
                    <w:left w:val="none"/>
                    <w:right w:val="none"/>
                </w:tcBorders>
            ''')
            cell._tc.get_or_add_tcPr().append(tcBorders)

    # ----------------------------------------------------
    # Header / Title Block
    # ----------------------------------------------------
    p_header = add_styled_paragraph(align=WD_ALIGN_PARAGRAPH.RIGHT, space_after=12)
    run_header = p_header.add_run("สื่อการเรียนรู้เชิงปฏิบัติการ: โครงงานนวัตกรรมดิจิทัล (IoT)")
    set_font_run(run_header, FONT_NAME, 12, italic=True, color=SECONDARY_COLOR)
    
    # Title
    p_title = add_styled_paragraph(align=WD_ALIGN_PARAGRAPH.CENTER, space_before=18, space_after=6)
    run_title = p_title.add_run("คู่มือการเรียนรู้เชิงปฏิบัติการ\nการพัฒนาโครงงานระบบจัดการสต็อกสินค้าอัตโนมัติด้วยเทคโนโลยี IoT\n(IoT-Based Automatic Inventory Management System)")
    set_font_run(run_title, FONT_NAME, 24, bold=True, color=PRIMARY_COLOR)
    
    p_subtitle = add_styled_paragraph(align=WD_ALIGN_PARAGRAPH.CENTER, space_after=24)
    run_sub = p_subtitle.add_run("หลักสูตรการเรียนรู้: เทคโนโลยีสมองกลฝังตัวและการเชื่อมต่อระบบคลาวด์")
    set_font_run(run_sub, FONT_NAME, 16, italic=True, color=ACCENT_COLOR)

    # Horizontal divider line
    p_div = doc.add_paragraph()
    p_div.alignment = WD_ALIGN_PARAGRAPH.CENTER
    p_div.paragraph_format.space_after = Pt(18)
    run_div = p_div.add_run("—" * 60)
    set_font_run(run_div, FONT_NAME, 12, color=SECONDARY_COLOR)

    # ----------------------------------------------------
    # Section 1: Introduction and Objectives
    # ----------------------------------------------------
    add_heading_1("1. บทนำและวัตถุประสงค์การเรียนรู้")
    
    p_intro = add_styled_paragraph()
    run_intro = p_intro.add_run(
        "ในยุคเศรษฐกิจดิจิทัล การบริหารจัดการสต็อกสินค้าอย่างมีประสิทธิภาพและแม่นยำมีความสำคัญเป็นอย่างมากสำหรับธุรกิจ "
        "โดยทั่วไปธุรกิจขนาดเล็กหรือร้านค้าปลีกมักจะใช้แรงงานคนในการตรวจนับสินค้า (Manual Counting) ซึ่งมักนำไปสู่ความล่าช้า "
        "ความคลาดเคลื่อน และการรายงานผลที่ไม่เป็นเรียลไทม์ โครงงานนี้จะพานักศึกษาไปเรียนรู้การสร้างนวัตกรรมคลังสินค้าอัจฉริยะ "
        "โดยอาศัยระบบเซ็นเซอร์ตรวจวัดน้ำหนักความละเอียดสูงในการนับชิ้นสินค้าอัตโนมัติ ประมวลผลผ่านไมโครคอนโทรลเลอร์ "
        "และส่งข้อมูลขึ้นระบบฐานข้อมูลคลาวด์เพื่ออัปเดตสถานะแบบเรียลไทม์ พร้อมแจ้งเตือนผู้ดูแลระบบผ่าน LINE Notify ทันทีเมื่อสต็อกมีการเปลี่ยนแปลง"
    )
    set_font_run(run_intro, FONT_NAME, 16, color=TEXT_COLOR)

    add_heading_2("วัตถุประสงค์การเรียนรู้")
    add_bullet_point("เพื่อเรียนรู้หลักการทำงานและการเชื่อมต่อเซ็นเซอร์วัดน้ำหนัก (Load Cell) ร่วมกับโมดูลแปลงสัญญาณ HX711")
    add_bullet_point("เพื่อเข้าใจกระบวนการแปลงสัญญาณ Analog เป็น Digital ความละเอียดสูง (24-bit Sigma-Delta ADC)")
    add_bullet_point("เพื่อศึกษาและพัฒนาโปรแกรมประมวลผลและการใช้ทฤษฎีการปัดเศษ (Threshold Ratio) เพื่อให้การนับจำนวนสินค้ามีความแม่นยำสูง")
    add_bullet_point("เพื่อเข้าใจวิธีการออกแบบและเชื่อมต่อระบบการรับส่งข้อมูลผ่านเครือข่ายไร้สาย (WiFi Auto-reconnect) ไปยังคลาวด์")
    add_bullet_point("เพื่อฝึกปฏิบัติการเก็บข้อมูลใน Time Series Database (InfluxDB) และเขียนโปรแกรมแจ้งเตือนแบบเรียลไทม์ผ่าน LINE Notify")

    # ----------------------------------------------------
    # Section 2: Equipment List
    # ----------------------------------------------------
    add_heading_1("2. รายการอุปกรณ์ประกอบการเรียนรู้")
    p_equip_desc = add_styled_paragraph("ตารางต่อไปนี้แสดงรายการฮาร์ดแวร์และอุปกรณ์หลักที่ใช้ในการพัฒนาโครงงานระบบจัดการสต็อกอัจฉริยะ:")
    set_font_run(p_equip_desc.runs[0], FONT_NAME, 16, color=TEXT_COLOR)

    # Equipment Table
    eq_table = doc.add_table(rows=6, cols=3)
    eq_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    style_table_header(eq_table.rows[0])
    
    # Headers
    headers = ["ลำดับ", "อุปกรณ์ / ส่วนประกอบ", "บทบาทและหน้าที่การใช้งาน"]
    for i, h in enumerate(headers):
        p = eq_table.cell(0, i).paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(h)
        set_font_run(run, FONT_NAME, 16, bold=True, color=RGBColor(255, 255, 255))
        
    eq_data = [
        ("1", "ESP32-C3 Supermini", "ไมโครคอนโทรลเลอร์หลักในการรับสัญญาณ ประมวลผลสูตรคำนวณ เชื่อมต่อ WiFi และควบคุมหน้าจอแสดงผล"),
        ("2", "Load Cell (PSD-S1)", "เซ็นเซอร์วัดน้ำหนักแบบแรงกดและแรงดึง (สามารถรับน้ำหนักได้สูงสุด 2 ตัน สำหรับนำมาประยุกต์ใช้กับสต็อกขนาดใหญ่)"),
        ("3", "HX711 Module", "โมดูลแปลงสัญญาณอนาล็อกขนาดเล็กจาก Load Cell เป็นสัญญาณดิจิทัลความละเอียด 24-bit Sigma-Delta ADC"),
        ("4", "ILI9341 2.8\" TFT Display", "หน้าจอสีแสดงผลขนาด 320x240 พิกเซล สำหรับแสดงจำนวนชิ้นสินค้า น้ำหนักรวม สถานะการเชื่อมต่อ และค่าดิบ (RAW Data)"),
        ("5", "Button Switch (Reset)", "ปุ่มสำหรับการสั่งงานล้างค่าน้ำหนักแท่นว่าง (Tare/Reset) หรือเข้าสู่หน้าโหมดสำหรับตั้งค่าคาลิเบรต (Calibration Mode)")
    ]
    
    for row_idx, data in enumerate(eq_data):
        row = eq_table.rows[row_idx + 1]
        style_table_row(row, is_even=(row_idx % 2 == 1))
        
        eq_table.cell(row_idx + 1, 0).width = Inches(0.8)
        eq_table.cell(row_idx + 1, 1).width = Inches(2.2)
        eq_table.cell(row_idx + 1, 2).width = Inches(3.0)
        
        for col_idx, text in enumerate(data):
            p = row.cells[col_idx].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT if col_idx > 0 else WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run(text)
            set_font_run(run, FONT_NAME, 14, color=TEXT_COLOR)

    # ----------------------------------------------------
    # Section 3: Theoretical Background
    # ----------------------------------------------------
    add_heading_1("3. ทฤษฎีและหลักการทำงานที่เกี่ยวข้อง")
    
    p_theory_intro = add_styled_paragraph("เพื่อให้นักศึกษาสามารถออกแบบระบบได้อย่างเข้าใจ ในส่วนนี้จะอธิบายทฤษฎีหลัก 4 ประการที่ใช้ในโครงงาน:")
    set_font_run(p_theory_intro.runs[0], FONT_NAME, 16, color=TEXT_COLOR)

    add_heading_2("3.1 ทฤษฎีสเตรนเกจ (Strain Gauge Theory)")
    p_sg = add_styled_paragraph(
        "ตัวเซ็นเซอร์ Load Cell ประกอบไปด้วยตัวรับน้ำหนักวัสดุอลูมิเนียมหรือเหล็กที่มี สเตรนเกจ (Strain Gauge) ติดตั้งอยู่ภายใน "
        "เมื่อมีแรงกดหรือน้ำหนักกระทำบนแท่นวาง จะส่งผลให้วัสดุเกิดการยืดหรือหดตัวเพียงเล็กน้อย (เกิดความเค้นและความเครียดเชิงกล) "
        "การเปลี่ยนแปลงรูปแบบเชิงกลนี้จะส่งผลโดยตรงต่อค่าความต้านทานไฟฟ้าของสเตรนเกจ ซึ่งเป็นไปตามปรากฏการณ์ที่เรียกว่า "
        "Piezoresistive Effect ซึ่งคำนวณตามสูตร:"
    )
    set_font_run(p_sg.runs[0], FONT_NAME, 16, color=TEXT_COLOR)
    
    add_formula_box(
        "ΔR/R = G × ε",
        [
            "ΔR = การเปลี่ยนแปลงของค่าความต้านทานไฟฟ้า (โอห์ม)",
            "R = ค่าความต้านทานเริ่มต้นของสเตรนเกจ (โอห์ม)",
            "G = ตัวคูณเกจ (Gauge Factor) ซึ่งแตกต่างกันตามชนิดของวัสดุตัวนำไฟฟ้า",
            "ε = ค่าความเครียด (Strain) หรืออัตราการเปลี่ยนรูปเชิงกลของวัสดุ"
        ]
    )

    add_heading_2("3.2 ทฤษฎีการแปลงสัญญาณอนาล็อกเป็นดิจิทัล (Analog-to-Digital Converter)")
    p_adc = add_styled_paragraph(
        "ค่าความต่างศักย์ไฟฟ้าที่ส่งมาจาก Load Cell จะมีขนาดเล็กมากในระดับมิลลิโวลต์ (mV) จึงไม่สามารถอ่านค่าผ่านอินพุต ADC "
        "ของไมโครคอนโทรลเลอร์ทั่วไปได้อย่างแม่นยำ จึงจำเป็นต้องใช้ชิปเฉพาะคือ HX711 ซึ่งประกอบด้วยเครื่องขยายสัญญาณรบกวนต่ำ "
        "(Low-Noise Amplifier) และตัวแปลงสัญญาณแบบ Sigma-Delta ADC ขนาด 24 บิต เพื่อแปลงสัญญาณดังกล่าวให้อยู่ในรูปข้อมูลดิจิทัลตามสูตร:"
    )
    set_font_run(p_adc.runs[0], FONT_NAME, 16, color=TEXT_COLOR)
    
    add_formula_box(
        "Digital Output = (Analog Input × Gain × 2^24) / Vref",
        [
            "Analog Input = แรงดันไฟฟ้าต่างศักย์ที่ป้อนเข้าจาก Load Cell (V)",
            "Gain = กำลังขยายสัญญาณของ HX711 (กำหนดค่าเป็น 64 หรือ 128 เท่าจากฝั่งขาอินพุต)",
            "2^24 = ความละเอียดสูงสุดของสัญญาณข้อมูล 24 บิต (เท่ากับ 16,777,216 ระดับ)",
            "Vref = แรงดันไฟฟ้าอ้างอิงภายในชิป (โดยทั่วไปมีค่าคงที่เท่ากับ 1.25V หรือ 2.5V ขึ้นอยู่กับการกำหนดโครงคอนฟิก)"
        ]
    )

    add_heading_2("3.3 การคำนวณค่าน้ำหนักจริงและการปรับจูน (Calibration)")
    p_cal = add_styled_paragraph(
        "เมื่อได้ค่าสัญญาณดิจิทัลดิบ (RAW) จาก HX711 แล้ว เราต้องนำมาหักล้างค่าน้ำหนักเริ่มต้นของตัวแท่นเปล่า (ค่าออฟเซ็ต: OFFSET) "
        "จากนั้นนำไปหารด้วยตัวประกอบสเกล (SCALE_FACTOR) เพื่อปรับให้ค่าที่ได้ตรงกับค่ามาตรฐาน เช่น กรัม หรือ กิโลกรัม:"
    )
    set_font_run(p_cal.runs[0], FONT_NAME, 16, color=TEXT_COLOR)
    
    add_formula_box(
        "WEIGHT = (RAW - OFFSET) / SCALE_FACTOR",
        [
            "WEIGHT = น้ำหนักของสินค้าจริงที่คำนวณได้ (กรัม/กิโลกรัม)",
            "RAW = ค่าดิจิทัลดิบที่อ่านได้จากโมดูล HX711 ขณะวางสินค้า",
            "OFFSET = ค่าดิจิทัลดิบที่อ่านได้จากโมดูล HX711 ในสภาวะไม่มีสิ่งของอยู่บนแท่น (Tare weight)",
            "SCALE_FACTOR = อัตราส่วนสเกลความสัมพันธ์ระหว่างน้ำหนักจริงต่อข้อมูลดิจิทัล"
        ]
    )
    
    p_sf_desc = add_styled_paragraph("สำหรับการหาค่า SCALE_FACTOR สามารถคำนวณได้จากการนำน้ำหนักที่ทราบค่ามาตรฐาน (Known Weight) มาวางทดสอบ:")
    set_font_run(p_sf_desc.runs[0], FONT_NAME, 16, color=TEXT_COLOR)

    add_formula_box(
        "SCALE_FACTOR = (KNOWN_WEIGHT_RAW - OFFSET) / KNOWN_WEIGHT",
        [
            "KNOWN_WEIGHT = น้ำหนักของวัตถุมาตรฐานที่เรารู้ค่าที่แน่นอน (เช่น วัตถุหนัก 1,000 กรัม)",
            "KNOWN_WEIGHT_RAW = ค่าดิจิทัลดิบจาก HX711 ที่อ่านได้เมื่อวางวัตถุมาตรฐานนั้นบนแท่น"
        ]
    )

    add_heading_2("3.4 การปัดเศษเพื่อคำนวณจำนวนชิ้นสินค้า (Rounding & Threshold Ratio)")
    p_round = add_styled_paragraph(
        "ในการนับจำนวนสินค้าจริง สินค้าแต่ละชิ้นมักมีความคลาดเคลื่อนของน้ำหนักเล็กน้อย (เช่น ซองขนมหนักเฉลี่ย 100 กรัม แต่บางซองหนัก 98 หรือ 102 กรัม) "
        "หากใช้สูตรการหารแบบธรรมดา (จำนวน = น้ำหนักรวม / น้ำหนักต่อหน่วย) อาจเกิดความคลาดเคลื่อนเป็นตัวเลขทศนิยม "
        "เพื่อแก้ปัญหานี้ โครงงานนี้ใช้ อัลกอริทึมการคำนวณการปัดเศษด้วยจุดตัดสินใจ (Threshold Ratio) ร่วมกับฟังก์ชันปัดเศษลง (Floor) ดังนี้:"
    )
    set_font_run(p_round.runs[0], FONT_NAME, 16, color=TEXT_COLOR)
    
    add_formula_box(
        "PACK_COUNT = FLOOR((WEIGHT / UNIT_WEIGHT) + THRESHOLD_RATIO)",
        [
            "PACK_COUNT = จำนวนชิ้นหรือจำนวนแพ็คของสินค้าที่คำนวณได้จริง (ชิ้น)",
            "WEIGHT = น้ำหนักรวมทั้งหมดที่วัดได้จากแท่นชั่ง",
            "UNIT_WEIGHT = น้ำหนักเฉลี่ยมาตรฐานต่อหน่วยของสินค้า 1 ชิ้น",
            "THRESHOLD_RATIO = อัตราส่วนจุดเปลี่ยนสำหรับการปัดเศษทศนิยม (ตัวอย่าง: ค่า 0.80 หรือ 80% หมายถึง หากน้ำหนักของสินค้ารวมเกินกว่า "
            "80% ของหน่วยน้ำหนักถัดไป จะปัดเศษจำนวนสินค้าขึ้นทันที ซึ่งจากผลทดลองในงานวิจัยพบว่าให้ความแม่นยำสูงที่สุดถึง 95%)"
        ]
    )

    # ----------------------------------------------------
    # Section 4: Hardware Connection
    # ----------------------------------------------------
    add_heading_1("4. แผนผังการต่อวงจรและขาสัญญาณ (Pin Mapping)")
    p_hw = add_styled_paragraph("เพื่อให้นักศึกษาสามารถต่ออุปกรณ์ได้อย่างถูกต้อง ให้ทำการเชื่อมต่อสายสัญญาณระหว่าง ESP32-C3, HX711, และ หน้าจอ TFT ตามตารางระบุขาสัญญาณต่อไปนี้:")
    set_font_run(p_hw.runs[0], FONT_NAME, 16, color=TEXT_COLOR)

    # Pin Map Table
    pin_table = doc.add_table(rows=10, cols=3)
    pin_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    style_table_header(pin_table.rows[0])
    
    pin_headers = ["อุปกรณ์ (Device)", "ขาสัญญาณของอุปกรณ์ (Pin)", "ขาต่อเข้ากับ ESP32-C3 (GPIO)"]
    for i, h in enumerate(pin_headers):
        p = pin_table.cell(0, i).paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(h)
        set_font_run(run, FONT_NAME, 16, bold=True, color=RGBColor(255, 255, 255))
        
    pin_data = [
        ("โมดูลขยายสัญญาณ HX711", "DT (Data)", "GPIO 3"),
        ("โมดูลขยายสัญญาณ HX711", "SCK (Clock)", "GPIO 2"),
        ("หน้าจอสี TFT Display (ILI9341)", "CS (Chip Select)", "GPIO 9"),
        ("หน้าจอสี TFT Display (ILI9341)", "DC (Data/Command)", "GPIO 7"),
        ("หน้าจอสี TFT Display (ILI9341)", "MOSI (SPI Data Out)", "GPIO 6"),
        ("หน้าจอสี TFT Display (ILI9341)", "SCK (SPI Clock)", "GPIO 4"),
        ("หน้าจอสี TFT Display (ILI9341)", "MISO (SPI Data In)", "GPIO 5"),
        ("ปุ่มสวิตช์รีเซ็ต (Button Reset)", "ขาอินพุตสวิตช์", "GPIO 20"),
        ("ปุ่มสวิตช์รีเซ็ต (Button Reset)", "ขาเอาต์พุตสวิตช์", "GND (Ground)")
    ]
    
    for row_idx, data in enumerate(pin_data):
        row = pin_table.rows[row_idx + 1]
        style_table_row(row, is_even=(row_idx % 2 == 1))
        
        pin_table.cell(row_idx + 1, 0).width = Inches(2.2)
        pin_table.cell(row_idx + 1, 1).width = Inches(1.8)
        pin_table.cell(row_idx + 1, 2).width = Inches(2.0)
        
        for col_idx, text in enumerate(data):
            p = row.cells[col_idx].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.LEFT if col_idx < 2 else WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run(text)
            set_font_run(run, FONT_NAME, 14, color=TEXT_COLOR)

    # ----------------------------------------------------
    # Section 5: Software & Code
    # ----------------------------------------------------
    add_heading_1("5. ขั้นตอนการเขียนโปรแกรมและการพัฒนาซอฟต์แวร์")
    
    p_sw = add_styled_paragraph("การพัฒนาโปรแกรมบน ESP32-C3 จะใช้โปรแกรม Arduino IDE ในการเขียน โดยประกอบด้วยขั้นตอนการทำงานและชุดคำสั่งสำคัญ 3 ส่วนย่อย ดังนี้:")
    set_font_run(p_sw.runs[0], FONT_NAME, 16, color=TEXT_COLOR)

    add_heading_2("5.1 การสอบเทียบน้ำหนักและเซ็ตค่า Offset (Calibration Setup)")
    p_code_1 = add_styled_paragraph(
        "ขั้นตอนแรกนักศึกษาต้องค้นหาค่าคงที่ในการชั่งน้ำหนัก โดยใช้โค้ดด้านล่างเพื่อเซ็ตค่าเฉลี่ยเริ่มต้น "
        "และทำการหาตัวสเกลหาร (SCALE_FACTOR) โดยวางวัตถุที่ทราบน้ำหนักแน่นอนเพื่อคำนวณค่าบันทึกไปใช้งานต่อ:"
    )
    set_font_run(p_code_1.runs[0], FONT_NAME, 16, color=TEXT_COLOR)

    code_block_1 = (
        "#include \"HX711.h\"\n\n"
        "const int LOADCELL_DOUT_PIN = 3;\n"
        "const int LOADCELL_SCK_PIN = 2;\n"
        "HX711 scale;\n\n"
        "void setup() {\n"
        "  Serial.begin(115200);\n"
        "  scale.begin(LOADCELL_DOUT_PIN, LOADCELL_SCK_PIN);\n"
        "  \n"
        "  Serial.println(\"กำลังล้างค่าน้ำหนักแท่นว่าง (Tare)... กรุณาอย่าเพิ่งวางของบนแท่นชั่ง\");\n"
        "  scale.set_scale();\n"
        "  scale.tare(); // เซ็ตค่าเริ่มต้น OFFSET เป็น 0\n"
        "  Serial.println(\"ล้างค่าน้ำหนักแท่นว่างสำเร็จ\");\n"
        "  \n"
        "  Serial.println(\"วางวัตถุน้ำหนักที่รู้ค่าแน่นอน (เช่น 1000 กรัม) แล้วกด Reset เพื่อนำไปหา SCALE_FACTOR\");\n"
        "}\n\n"
        "void loop() {\n"
        "  if (scale.is_ready()) {\n"
        "    long reading = scale.get_units(10);\n"
        "    Serial.print(\"Raw Reading (Average of 10): \");\n"
        "    Serial.println(reading);\n"
        "  }\n"
        "  delay(1000);\n"
        "}"
    )
    add_code_block(code_block_1)

    add_heading_2("5.2 ฟังก์ชันคำนวณจำนวนชิ้นสินค้าและการแสดงผล (Counting and Display)")
    p_code_2 = add_styled_paragraph(
        "ตัวอย่างฟังก์ชันในการนำน้ำหนักที่ได้มาหารด้วยน้ำหนักมาตรฐานของสินค้า 1 ชิ้น (UNIT_WEIGHT) "
        "โดยประยุกต์ใช้อัตราการปัดเศษ (THRESHOLD_RATIO = 0.80) เพื่อคำนวณจำนวนชิ้นและส่งผลขึ้นหน้าจอ TFT และ Serial Monitor:"
    )
    set_font_run(p_code_2.runs[0], FONT_NAME, 16, color=TEXT_COLOR)

    code_block_2 = (
        "float scale_factor = 22.8;    // ตัวอย่างค่าตัวประกอบสเกลที่ได้จากการคาลิเบรต\n"
        "float unit_weight = 100.0;    // น้ำหนักมาตรฐานของสินค้า 1 ชิ้น (กรัม)\n"
        "float threshold_ratio = 0.80; // จุดปัดเศษทศนิยม (80%)\n\n"
        "int calculate_packs(float total_weight) {\n"
        "  float raw_count = total_weight / unit_weight;\n"
        "  int count_floor = (int)raw_count;\n"
        "  float fraction = raw_count - count_floor;\n"
        "  \n"
        "  if (fraction >= threshold_ratio) {\n"
        "    return count_floor + 1; // ปัดเศษขึ้นเมื่อสัดส่วนเกิน 80%\n"
        "  } else {\n"
        "    return count_floor;     // ปัดเศษลงเมื่อไม่ถึงเกณฑ์\n"
        "  }\n"
        "}\n\n"
        "void update_system() {\n"
        "  scale.set_scale(scale_factor);\n"
        "  float weight = scale.get_units(5);\n"
        "  if (weight < 0) weight = 0; // ป้องกันปัญหาน้ำหนักแสดงผลติดลบเล็กน้อย\n"
        "  \n"
        "  int items = calculate_packs(weight);\n"
        "  Serial.print(\"Weight: \"); Serial.print(weight); Serial.print(\" g | \");\n"
        "  Serial.print(\"Packs: \"); Serial.println(items);\n"
        "  // โค้ดส่งข้อมูลไปแสดงผลที่หน้าจอ TFT\n"
        "}"
    )
    add_code_block(code_block_2)

    add_heading_2("5.3 การเชื่อมต่อ WiFi, คลาวด์ InfluxDB และ LINE Notify")
    p_code_3 = add_styled_paragraph(
        "โปรแกรมหลักในขั้นตอนนี้จะทำการตรวจสอบสถานะ WiFi แบบอัตโนมัติ (Auto-reconnect) "
        "หากมีการเปลี่ยนแปลงยอดสต็อกสินค้าที่คงที่และเสถียร ระบบจะส่งค่าน้ำหนักและจำนวนสินค้าชิ้นปัจจุบันไปยัง InfluxDB Cloud "
        "และส่งข้อความสรุปแจ้งเตือนรายวันหรือแจ้งยอดเข้าห้องแชตผ่าน LINE API โดยการเรียกใช้ Web App Script หรือใช้ LINE API โดยตรง:"
    )
    set_font_run(p_code_3.runs[0], FONT_NAME, 16, color=TEXT_COLOR)

    code_block_3 = (
        "#include <WiFi.h>\n"
        "#include <HTTPClient.h>\n\n"
        "const char* ssid = \"Your_WiFi_SSID\";\n"
        "const char* password = \"Your_WiFi_Password\";\n"
        "const char* line_token = \"YOUR_LINE_NOTIFY_TOKEN\";\n\n"
        "void connectWiFi() {\n"
        "  WiFi.begin(ssid, password);\n"
        "  while (WiFi.status() != WL_CONNECTED) {\n"
        "    delay(500); Serial.print(\".\");\n"
        "  }\n"
        "  Serial.println(\"เชื่อมต่อ WiFi สำเร็จ\");\n"
        "}\n\n"
        "void sendLineNotification(String message) {\n"
        "  if (WiFi.status() == WL_CONNECTED) {\n"
        "    HTTPClient http;\n"
        "    http.begin(\"https://notify-api.line.me/api/notify\");\n"
        "    http.addHeader(\"Content-Type\", \"application/x-www-form-urlencoded\");\n"
        "    http.addHeader(\"Authorization\", \"Bearer \" + String(line_token));\n"
        "    \n"
        "    String postData = \"message=\" + message;\n"
        "    int httpCode = http.POST(postData);\n"
        "    if (httpCode > 0) {\n"
        "      Serial.println(\"ส่งการแจ้งเตือน LINE สำเร็จ\");\n"
        "    } else {\n"
        "      Serial.println(\"เกิดข้อผิดพลาดในการส่ง LINE\");\n"
        "    }\n"
        "    http.end();\n"
        "  }\n"
        "}"
    )
    add_code_block(code_block_3)

    # ----------------------------------------------------
    # Section 6: Laboratory Exercises
    # ----------------------------------------------------
    doc.add_page_break()
    add_heading_1("6. กิจกรรมการทดลองปฏิบัติการ (Lab Sheets)")
    
    p_lab_intro = add_styled_paragraph(
        "ใบงานปฏิบัตินี้จัดขึ้นเพื่อให้นักศึกษาทำการบันทึกและวิเคราะห์ค่าความถูกต้องของการทดลองจากการพัฒนาระบบจริง "
        "โดยแบ่งออกเป็น 2 กิจกรรมย่อย:"
    )
    set_font_run(p_lab_intro.runs[0], FONT_NAME, 16, color=TEXT_COLOR)

    add_heading_2("กิจกรรมที่ 6.1: การหาค่าความแม่นยำในการนับสินค้าตามอัตราปัดเศษ (Threshold Ratio)")
    p_lab1_desc = add_styled_paragraph(
        "คำชี้แจง: ให้นักศึกษาชั่งสินค้าทีละชิ้นตั้งแต่ 1 ชิ้น จนครบ 20 ชิ้น โดยทำการทดลองซ้ำด้วยการป้อนอัตราการปัดเศษ (Threshold Ratio) "
        "ที่ระดับต่างๆ (20%, 40%, 60%, 80%) และบันทึกผลการคำนวณจำนวนชิ้นที่ระบบวัดได้ จากนั้นวิเคราะห์หาค่าเฉลี่ยความถูกต้อง (Accuracy %)"
    )
    set_font_run(p_lab1_desc.runs[0], FONT_NAME, 16, color=TEXT_COLOR)

    # Table for Lab 1
    lab1_table = doc.add_table(rows=6, cols=5)
    lab1_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    style_table_header(lab1_table.rows[0])
    
    lab1_headers = ["จำนวนจริง (ชิ้น)", "ผลลัพธ์ที่วัดได้ (เกณฑ์ 20%)", "ผลลัพธ์ที่วัดได้ (เกณฑ์ 40%)", "ผลลัพธ์ที่วัดได้ (เกณฑ์ 60%)", "ผลลัพธ์ที่วัดได้ (เกณฑ์ 80%)"]
    for i, h in enumerate(lab1_headers):
        p = lab1_table.cell(0, i).paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(h)
        set_font_run(run, FONT_NAME, 14, bold=True, color=RGBColor(255, 255, 255))
        
    lab1_rows = [
        ("1 - 5 ชิ้น", "", "", "", ""),
        ("6 - 10 ชิ้น", "", "", "", ""),
        ("11 - 15 ชิ้น", "", "", "", ""),
        ("16 - 20 ชิ้น", "", "", "", ""),
        ("สรุปค่าความถูกต้องเฉลี่ย (%)", "........ %", "........ %", "........ %", "........ %")
    ]
    
    for row_idx, data in enumerate(lab1_rows):
        row = lab1_table.rows[row_idx + 1]
        style_table_row(row, is_even=(row_idx % 2 == 1))
        
        lab1_table.cell(row_idx + 1, 0).width = Inches(1.8)
        for c in range(1, 5):
            lab1_table.cell(row_idx + 1, c).width = Inches(1.2)
            
        for col_idx, text in enumerate(data):
            p = row.cells[col_idx].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run(text)
            
            is_bold = (row_idx == len(lab1_rows) - 1)
            set_font_run(run, FONT_NAME, 14, bold=is_bold, color=TEXT_COLOR)

    add_heading_2("กิจกรรมที่ 6.2: การเปรียบเทียบความเร็วในการตรวจสต็อกสินค้า (Manual vs IoT)")
    p_lab2_desc = add_styled_paragraph(
        "คำชี้แจง: ให้นักศึกษาทดลองนับและบันทึกข้อมูลสินค้าด้วยตัวเอง (ใช้กระดาษจดบันทึก) เปรียบเทียบกับระบบอัปเดตอัตโนมัติผ่านคลาวด์ "
        "บันทึกระยะเวลาที่ใช้ในการบันทึกข้อมูลเมื่อจำนวนสินค้ามีปริมาณต่างๆ กัน:"
    )
    set_font_run(p_lab2_desc.runs[0], FONT_NAME, 16, color=TEXT_COLOR)

    # Table for Lab 2
    lab2_table = doc.add_table(rows=5, cols=3)
    lab2_table.alignment = WD_TABLE_ALIGNMENT.CENTER
    style_table_header(lab2_table.rows[0])
    
    lab2_headers = ["จำนวนปริมาณสินค้าที่ทดสอบ (ชิ้น)", "เวลาเฉลี่ยการนับและลงบันทึกด้วยมือ (วินาที)", "เวลาประมวลผลและส่งคลาวด์ของระบบ IoT (วินาที)"]
    for i, h in enumerate(lab2_headers):
        p = lab2_table.cell(0, i).paragraphs[0]
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        run = p.add_run(h)
        set_font_run(run, FONT_NAME, 14, bold=True, color=RGBColor(255, 255, 255))
        
    lab2_rows = [
        ("10 ชิ้น", "........ วินาที", "........ วินาที"),
        ("20 ชิ้น", "........ วินาที", "........ วินาที"),
        ("30 ชิ้น", "........ วินาที", "........ วินาที"),
        ("40 ชิ้น", "........ วินาที", "........ วินาที")
    ]
    
    for row_idx, data in enumerate(lab2_rows):
        row = lab2_table.rows[row_idx + 1]
        style_table_row(row, is_even=(row_idx % 2 == 1))
        
        lab2_table.cell(row_idx + 1, 0).width = Inches(2.2)
        lab2_table.cell(row_idx + 1, 1).width = Inches(2.0)
        lab2_table.cell(row_idx + 1, 2).width = Inches(2.0)
        
        for col_idx, text in enumerate(data):
            p = row.cells[col_idx].paragraphs[0]
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
            run = p.add_run(text)
            set_font_run(run, FONT_NAME, 14, color=TEXT_COLOR)

    # ----------------------------------------------------
    # Section 7: Discussion and Self-Assessment
    # ----------------------------------------------------
    add_heading_1("7. คำถามท้ายกิจกรรมและการอภิปรายผล")
    
    p_ques_intro = add_styled_paragraph("ให้นักศึกษาตอบคำถามและร่วมกันสรุปอภิปรายประเด็นดังต่อไปนี้ลงในสมุดรายงานปฏิบัติการ:")
    set_font_run(p_ques_intro.runs[0], FONT_NAME, 16, color=TEXT_COLOR)
    
    questions = [
        "1) เพราะเหตุใดเราจึงไม่ใช้วิธีนำค่าน้ำหนักรวมทั้งหมดหารด้วยน้ำหนักชิ้นเดี่ยวตรงๆ (ไม่มีการปัดเศษด้วย Threshold) ในการรายงานจำนวนสินค้าจริง?",
        "2) จากการทดลอง ผลการหาความแม่นยำ (Accuracy) ที่อัตราการปัดเศษ (Threshold Ratio) ที่ระดับใดดีที่สุด และเพราะเหตุใดจึงเป็นเช่นนั้น?",
        "3) ปัญหาด้านอุณหภูมิของสภาพแวดล้อมโดยรอบมีผลต่อความถูกต้องในการชั่งน้ำหนักของเซ็นเซอร์ Load Cell หรือไม่ อย่างไร? และสามารถเสนอแนวทางแก้ไขได้อย่างไร?",
        "4) หากระบบขาดการเชื่อมต่อ WiFi (WiFi Drop) โค้ดโปรแกรมในส่วน auto-reconnect มีความสำคัญอย่างไรเพื่อไม่ให้ข้อมูลรายงานผิดพลาดหรือสูญหาย?",
        "5) จงระบุแนวคิดในการนำเอาระบบจัดการสต็อกอัจฉริยะ IoT ชิ้นนี้ ไปประยุกต์ใช้งานหรือพัฒนาต่อยอดในชีวิตจริงเพิ่มเติม (เช่น ภาคอุตสาหกรรม การเกษตร หรือชีวิตประจำวัน)"
    ]
    
    for q in questions:
        p_q = add_styled_paragraph()
        p_q.paragraph_format.left_indent = Inches(0.25)
        run_q = p_q.add_run(q)
        set_font_run(run_q, FONT_NAME, 16, color=TEXT_COLOR)
        
        p_ans = add_styled_paragraph("ตอบ: ............................................................................................................................................................................................")
        p_ans.paragraph_format.left_indent = Inches(0.5)
        set_font_run(p_ans.runs[0], FONT_NAME, 14, italic=True, color=SECONDARY_COLOR)

    # Save to file
    out_dir = os.path.dirname(os.path.abspath(__file__))
    out_path = os.path.join(out_dir, "คู่มือการเรียนรู้_ระบบจัดการสต็อกสินค้าด้วย_IoT.docx")
    doc.save(out_path)
    print(f"Document created successfully at: {out_path}")

if __name__ == "__main__":
    create_document()
