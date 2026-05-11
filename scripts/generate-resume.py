#!/usr/bin/env python3
"""Generate updated resume PDF for Kridtin Chawalratikool."""

import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY, TA_RIGHT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle, KeepTogether
from reportlab.lib import colors
from reportlab.lib.colors import black, HexColor

OUT = os.path.join(os.path.dirname(__file__), '..', 'static', 'resume.pdf')

W, H = letter

doc = SimpleDocTemplate(
    OUT,
    pagesize=letter,
    rightMargin=0.75 * inch,
    leftMargin=0.75 * inch,
    topMargin=0.6 * inch,
    bottomMargin=0.6 * inch,
)

GRAY = HexColor('#444444')
LGRAY = HexColor('#666666')

def s(name, **kw):
    base = dict(fontName='Helvetica', fontSize=9.5, textColor=black, leading=13)
    base.update(kw)
    return ParagraphStyle(name, **base)

styles = {
    'name':    s('name', fontName='Helvetica-Bold', fontSize=17, alignment=TA_CENTER, spaceAfter=3),
    'contact': s('contact', fontSize=9, alignment=TA_CENTER, spaceAfter=6, textColor=GRAY),
    'bio':     s('bio', fontName='Helvetica-Oblique', fontSize=9.5, alignment=TA_JUSTIFY, spaceAfter=6, leading=14),
    'section': s('section', fontName='Helvetica-Bold', fontSize=12, spaceBefore=10, spaceAfter=5),
    'co_l':    s('co_l', fontName='Helvetica-Bold', fontSize=10, spaceAfter=0),
    'co_r':    s('co_r', fontName='Helvetica-Bold', fontSize=10, alignment=TA_RIGHT, spaceAfter=0),
    'role_l':  s('role_l', fontName='Helvetica-Oblique', fontSize=9.5, spaceAfter=3),
    'role_r':  s('role_r', fontName='Helvetica-Oblique', fontSize=9.5, alignment=TA_RIGHT, spaceAfter=3),
    'bullet':  s('bullet', leftIndent=14, spaceAfter=1.5, leading=13),
    'normal':  s('normal', spaceAfter=3),
    'bold':    s('bold', fontName='Helvetica-Bold', spaceAfter=2),
    'note':    s('note', fontName='Helvetica-Oblique', fontSize=9, textColor=LGRAY, spaceAfter=4),
    'edu':     s('edu', spaceAfter=3),
}

def row(left_text, right_text, left_style, right_style):
    pw = W - 1.5 * inch
    t = Table([[Paragraph(left_text, styles[left_style]),
                Paragraph(right_text, styles[right_style])]],
              colWidths=[pw * 0.65, pw * 0.35])
    t.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 2),
    ]))
    return t

def bullet(text):
    return Paragraph(f'- &nbsp; {text}', styles['bullet'])

story = []

# ── Header ────────────────────────────────────────────────────────────────────
story.append(Paragraph('Kridtin Chawalratikool', styles['name']))
story.append(Paragraph(
    'kridtin.ch@gmail.com &nbsp;|&nbsp; 083-038-2618 &nbsp;|&nbsp; '
    'github.com/kridtinc &nbsp;|&nbsp; linkedin.com/in/kridtinc',
    styles['contact']
))
story.append(Paragraph(
    'A Software Engineer with 6 years of experience, specializing in the architectural design '
    'and development of end-to-end applications. My primary programming languages are Go and '
    'TypeScript, but also eager to explore new languages, tools, and techniques to further '
    'enhance my knowledge and skillset.',
    styles['bio']
))
story.append(HRFlowable(width='100%', thickness=1, color=black, spaceAfter=6))

# ── Skills ────────────────────────────────────────────────────────────────────
story.append(Paragraph('Skills', styles['section']))

story.append(Paragraph(
    '<b>Experienced:</b> Go, TypeScript, Java, Python, SQL, React, Next.js, Vue, Nuxt, '
    'MySQL, MongoDB, YottaDB, Redis, GraphQL, gRPC, Kafka, RabbitMQ, Apache Airflow, '
    'Docker, Git, GitHub Actions, Shell',
    styles['normal']
))
story.append(Paragraph(
    '<b>Familiar:</b> Node.js, Express.js, Elasticsearch, NGINX, BMC Control-M, '
    'AWS (EC2, S3, DynamoDB, Lambda), GCP (GCE, GCR), K8s, Kotlin',
    styles['normal']
))
story.append(Paragraph(
    '<b>AI &amp; Tools:</b> Cursor AI, Model Context Protocol (MCP), Context Engineering',
    styles['normal']
))

# ── Experience ────────────────────────────────────────────────────────────────
story.append(Paragraph('Experiences', styles['section']))

# LINE MAN Wongnai
story.append(KeepTogether([
    row('LINE MAN Wongnai', 'Bangkok, TH · Hybrid', 'co_l', 'co_r'),
    row('Senior Software Engineer', 'Oct 2024 – Present', 'role_l', 'role_r'),
    Paragraph('<i>Promoted to Senior Software Engineer · Feb 2026</i>', styles['note']),
    bullet('Key contributor in launching the new LINE MAN product from the ground up'),
    bullet('Took initiative in team setup, culture-building, and defining workflows for a newly formed team'),
    bullet('Facilitated discussions, shared updates, and improved processes through EM/PM collaboration'),
    bullet('Drove effective cross-team communication with other service owners'),
    bullet('Translated product features into actionable tasks, ensuring clarity and alignment within the team'),
    bullet('Proactively worked with PM to assess feasibility, communicate technical constraints, and align on solutions'),
    bullet('Delivered high-quality, on-time implementations with strong ownership from design to deployment'),
    Spacer(1, 6),
]))

# LINE Company
story.append(KeepTogether([
    row('LINE Company (Thailand)', 'Bangkok, TH · Hybrid', 'co_l', 'co_r'),
    row('Solution Engineer', 'Jul 2022 – Aug 2024', 'role_l', 'role_r'),
    bullet('Developed new features for Social Commerce Platform (LINE Shopping, MyShop) to enhance user experience and drive engagement'),
    bullet('Collaborated with cross-functional teams to implement effective solutions for requirements breakdown, ensuring seamless integration'),
    bullet('Conducted demonstrations with the business team to showcase new features, leading to successful product launches'),
    bullet('Provided timely support for incidents, investigating issues to ensure customer satisfaction'),
    Spacer(1, 6),
]))

# KBTG
story.append(KeepTogether([
    row('KASIKORN Business-Technology Group (KBTG)', 'Nonthaburi, TH · Hybrid', 'co_l', 'co_r'),
    row('Software Engineer', 'Jul 2020 – Jun 2022', 'role_l', 'role_r'),
    bullet('Implemented Centralized Back Office financial application for KBank users with various features'),
    bullet('Designed databases and technical flows to meet business requirements with a focus on performance optimization'),
    bullet('Created Control-M specifications for system batch processes'),
    bullet('Developed and tested REST APIs for client web applications; utilized gRPC following SOLID and Clean Architecture principles'),
    bullet('Conducted code peer reviews to ensure accuracy of business logic and performed unit testing'),
    bullet('Improved the automated test pipeline to provide more readable and trackable logs for easier identification of failed tests'),
    bullet('Provided support to the test team and NFT team in identifying and resolving functional defects and performance issues'),
    bullet('Assisted the Technical Lead in deployment processes and incident resolution'),
    Spacer(1, 6),
]))

# True Corporation
story.append(KeepTogether([
    row('True Corporation', 'Bangkok, TH', 'co_l', 'co_r'),
    row('Full Stack Web Developer (Internship)', 'Jun 2019 – Aug 2019', 'role_l', 'role_r'),
    bullet('Collaborated with the team lead to design the architecture diagram and POC for a billing inquiry system using the MVC pattern'),
    bullet('Developed an online customer billing website to enable customers to inquire about their invoices and receipts'),
    bullet('Implemented APIs to gather data from the company\'s existing billing data stored in relational databases'),
    bullet('Developed APIs to generate invoices and receipts as PDF files using the Jasper Report file format'),
    Spacer(1, 6),
]))

# ── Volunteering ──────────────────────────────────────────────────────────────
story.append(Paragraph('Volunteering', styles['section']))
story.append(KeepTogether([
    row('LINE Company (Thailand) — Solution Engineer', 'May 2023 · 1 mo', 'co_l', 'co_r'),
    bullet('Served as a host for Go training sessions for the LINE Rookie (Intern) program'),
    Spacer(1, 4),
]))
story.append(KeepTogether([
    row('Chulalongkorn University — Teaching Staff', 'May 2017 · 1 mo', 'co_l', 'co_r'),
    bullet('Taught Python programming to high school students'),
    Spacer(1, 4),
]))

# ── Education ─────────────────────────────────────────────────────────────────
story.append(Paragraph('Education', styles['section']))
story.append(Paragraph(
    'Bachelor of Engineering in Computer Engineering, Chulalongkorn University (2020), 3.09 GPA',
    styles['edu']
))

doc.build(story)
print(f'✓ Resume written to {os.path.abspath(OUT)}')
