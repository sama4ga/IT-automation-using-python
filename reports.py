#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def generate_report(filename, title, paragraph):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  paragraph = Paragraph(paragraph, styles['BodyText'])
  report.build(report_title, Spacer(1, 20), paragraph)
  
  # empty_line = Spacer(1, 10)
  # lines = [report_title, Spacer(1, 20)]

  # for line in paragraph:
  #   lines.append(Paragraph(line, styles['BodyText'])) 
  #   lines.append(empty_line)
  # report.build(lines)