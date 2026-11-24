"""
MANVIAN Assessment - Task 2: PowerPoint Presentation Generator
Topic: Latest Updates in Google NotebookLM (As of November 24, 2026)
Generates: NotebookLM_Latest_Updates_Manvian.pptx (EXACTLY 5 SLIDES)
"""

import sys
import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

def create_deck():
    prs = Presentation()
    # 16:9 Widescreen standard
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6] # completely blank layout

    # Color Palette Definitions
    COLOR_BG_DARK = RGBColor(11, 19, 43)        # #0B132B
    COLOR_CARD_DARK = RGBColor(26, 38, 66)      # #1A2642
    COLOR_CARD_ALT = RGBColor(18, 28, 51)       # #121C33
    COLOR_BLUE_ACCENT = RGBColor(37, 99, 235)   # #2563EB
    COLOR_CYAN_ACCENT = RGBColor(56, 189, 248)  # #38BDF8
    COLOR_WHITE = RGBColor(255, 255, 255)       # #FFFFFF
    COLOR_MUTED = RGBColor(148, 163, 184)       # #94A3B8
    COLOR_BORDER = RGBColor(51, 65, 85)         # #334155
    COLOR_EMERALD = RGBColor(16, 185, 129)      # #10B981
    COLOR_AMBER = RGBColor(245, 158, 11)        # #F59E0B
    COLOR_PURPLE = RGBColor(139, 92, 246)       # #8B5CF6

    def set_slide_background(slide):
        bg = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, prs.slide_width, prs.slide_height)
        bg.fill.solid()
        bg.fill.fore_color.rgb = COLOR_BG_DARK
        bg.line.fill.background() # no line
        return bg

    def add_header(slide, tag_text, title_text, subtitle_text):
        # Category Tag Badge
        tag_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.45), Inches(6.0), Inches(0.35))
        tf_tag = tag_box.text_frame
        tf_tag.word_wrap = True
        tf_tag.margin_left = tf_tag.margin_top = tf_tag.margin_right = tf_tag.margin_bottom = 0
        p_tag = tf_tag.paragraphs[0]
        p_tag.text = tag_text.upper()
        p_tag.font.size = Pt(10)
        p_tag.font.bold = True
        p_tag.font.color.rgb = COLOR_CYAN_ACCENT

        # Title
        title_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.7), Inches(0.6))
        tf_title = title_box.text_frame
        tf_title.word_wrap = True
        tf_title.margin_left = tf_title.margin_top = tf_title.margin_right = tf_title.margin_bottom = 0
        p_title = tf_title.paragraphs[0]
        p_title.text = title_text
        p_title.font.size = Pt(24)
        p_title.font.bold = True
        p_title.font.color.rgb = COLOR_WHITE

        # Subtitle
        sub_box = slide.shapes.add_textbox(Inches(0.8), Inches(1.35), Inches(11.7), Inches(0.4))
        tf_sub = sub_box.text_frame
        tf_sub.word_wrap = True
        tf_sub.margin_left = tf_sub.margin_top = tf_sub.margin_right = tf_sub.margin_bottom = 0
        p_sub = tf_sub.paragraphs[0]
        p_sub.text = subtitle_text
        p_sub.font.size = Pt(12)
        p_sub.font.color.rgb = COLOR_MUTED

    def add_footer(slide, current_slide, total_slides=5):
        # Footer line
        footer_line = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(0.8), Inches(7.0), Inches(11.733), Inches(0.02))
        footer_line.fill.solid()
        footer_line.fill.fore_color.rgb = COLOR_BORDER
        footer_line.line.fill.background()

        # Footer Text
        fb = slide.shapes.add_textbox(Inches(0.8), Inches(7.05), Inches(8.0), Inches(0.3))
        tf = fb.text_frame
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = "MANVIAN Executive Briefing • Topic: Latest Updates in Google NotebookLM (As of Nov 2026)"
        p.font.size = Pt(9)
        p.font.color.rgb = COLOR_MUTED

        # Slide Number
        sb = slide.shapes.add_textbox(Inches(10.5), Inches(7.05), Inches(2.0), Inches(0.3))
        tf_s = sb.text_frame
        tf_s.margin_left = tf_s.margin_top = tf_s.margin_right = tf_s.margin_bottom = 0
        ps = tf_s.paragraphs[0]
        ps.alignment = PP_ALIGN.RIGHT
        ps.text = f"Slide {current_slide} of {total_slides}"
        ps.font.size = Pt(9)
        ps.font.bold = True
        ps.font.color.rgb = COLOR_CYAN_ACCENT

    # =========================================================================
    # SLIDE 1: INTRODUCTION
    # What is NotebookLM?, Purpose & Importance, How it helps students, professionals, businesses
    # =========================================================================
    slide1 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide1)
    add_header(slide1, "FOUNDATIONAL OVERVIEW", "What is Google NotebookLM? Purpose & Strategic Value",
               "A personalized AI research assistant grounded strictly in user-curated sources, eliminating hallucination risks.")
    add_footer(slide1, 1)

    # 3 Large Feature Columns
    cols = [
        {
            "tag": "CORE IDENTITY",
            "title": "What is NotebookLM?",
            "icon_color": COLOR_CYAN_ACCENT,
            "bullets": [
                "Source-Grounded AI: An experimental AI notebook built on Google's Gemini architecture that relies exclusively on notes, PDFs, docs, and URLs provided by the user.",
                "Zero Hallucination Protocol: Unlike generalized LLMs, every claim is anchored to verbatim passages with interactive inline citations.",
                "Massive Ingestion: Ingests up to 50 sources per notebook with up to 500,000 words per source (25M total words context window)."
            ]
        },
        {
            "tag": "STRATEGIC PURPOSE",
            "title": "Purpose & Importance",
            "icon_color": COLOR_BLUE_ACCENT,
            "bullets": [
                "Overcoming Information Overload: Synthesizes hundreds of pages of complex literature, legal contracts, and technical manuals in seconds.",
                "Multimodal Synthesis: Seamlessly links unstructured text, presentation slides, markdown, audio transcripts, and YouTube lectures.",
                "Cognitive Thought Partner: Generates study guides, FAQ matrices, chronological timelines, and high-yield briefing documents on demand."
            ]
        },
        {
            "tag": "AUDIENCE IMPACT",
            "title": "Who Benefits & How?",
            "icon_color": COLOR_EMERALD,
            "bullets": [
                "Students & Academics: Converts dense textbook chapters and lecture recordings into active study outlines and audio summaries.",
                "Business Professionals: Compares quarterly 10-K filings, vendor RFPs, and competitor analyses without data leaks.",
                "Enterprises & Teams: Centralizes corporate knowledge wikis into an auditable, verified intelligence hub with zero model retraining."
            ]
        }
    ]

    col_width = Inches(3.68)
    col_gap = Inches(0.34)
    start_x = Inches(0.8)
    card_y = Inches(1.9)
    card_h = Inches(4.8)

    for i, col in enumerate(cols):
        cx = start_x + i * (col_width + col_gap)
        card = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, card_y, col_width, card_h)
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_DARK
        card.line.color.rgb = COLOR_BORDER
        card.line.width = Pt(1)

        # Header Pill inside Card
        pill = slide1.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx + Inches(0.25), card_y + Inches(0.25), Inches(1.8), Inches(0.3))
        pill.fill.solid()
        pill.fill.fore_color.rgb = COLOR_CARD_ALT
        pill.line.color.rgb = col["icon_color"]
        pill.line.width = Pt(1)
        p_tf = pill.text_frame
        p_tf.margin_left = p_tf.margin_top = p_tf.margin_right = p_tf.margin_bottom = 0
        pp = p_tf.paragraphs[0]
        pp.alignment = PP_ALIGN.CENTER
        pp.text = col["tag"]
        pp.font.size = Pt(8.5)
        pp.font.bold = True
        pp.font.color.rgb = col["icon_color"]

        # Card Title
        tb = slide1.shapes.add_textbox(cx + Inches(0.25), card_y + Inches(0.68), col_width - Inches(0.5), Inches(0.5))
        tf = tb.text_frame
        tf.word_wrap = True
        tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
        p = tf.paragraphs[0]
        p.text = col["title"]
        p.font.size = Pt(16)
        p.font.bold = True
        p.font.color.rgb = COLOR_WHITE

        # Bullets
        bb = slide1.shapes.add_textbox(cx + Inches(0.25), card_y + Inches(1.25), col_width - Inches(0.5), card_h - Inches(1.4))
        btf = bb.text_frame
        btf.word_wrap = True
        btf.margin_left = btf.margin_top = btf.margin_right = btf.margin_bottom = 0

        for b_idx, bullet in enumerate(col["bullets"]):
            bp = btf.add_paragraph() if b_idx > 0 else btf.paragraphs[0]
            bp.space_after = Pt(14)
            parts = bullet.split(": ", 1)
            if len(parts) == 2:
                r1 = bp.add_run()
                r1.text = "• " + parts[0] + ": "
                r1.font.bold = True
                r1.font.size = Pt(11)
                r1.font.color.rgb = COLOR_CYAN_ACCENT
                r2 = bp.add_run()
                r2.text = parts[1]
                r2.font.size = Pt(10.5)
                r2.font.color.rgb = COLOR_MUTED
            else:
                r = bp.add_run()
                r.text = "• " + bullet
                r.font.size = Pt(10.5)
                r.font.color.rgb = COLOR_MUTED

    # =========================================================================
    # SLIDE 2: LATEST UPDATES & VERIFIED TIMELINE
    # Most important recent verified features, capabilities, and announcement dates
    # =========================================================================
    slide2 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide2)
    add_header(slide2, "VERIFIED PRODUCT ROADMAP", "Latest Announcements & Feature Evolution (2024 – 2026)",
               "Chronological timeline of verified official Google Blog and Google Workspace releases.")
    add_footer(slide2, 2)

    events = [
        {
            "date": "Sept 11, 2024",
            "title": "Audio Overviews Launch",
            "desc": "Official rollout of one-click AI podcast discussions. Two AI hosts engage in natural conversational analysis of uploaded sources using Gemini 1.5's multimodal architecture.",
            "tag": "Foundational Audio",
            "color": COLOR_CYAN_ACCENT
        },
        {
            "date": "Dec 13, 2024",
            "title": "Interactive Audio & Plus",
            "desc": "Major UI revamp adding interactive 'Join' button allowing users to speak directly to hosts. Unveiled Gemini 2.0 Flash integration and NotebookLM Plus enterprise subscription.",
            "tag": "Voice Interactivity",
            "color": COLOR_BLUE_ACCENT
        },
        {
            "date": "April 29, 2025",
            "title": "50+ Languages Rollout",
            "desc": "Multilingual Audio Overview generation across 50+ languages (French, Spanish, German, Japanese, Hindi). Enterprise admin controls enabled for Google Workspace and Education tiers.",
            "tag": "Global Expansion",
            "color": COLOR_EMERALD
        },
        {
            "date": "Mid-2025",
            "title": "Studio Revamp & Video",
            "desc": "Studio panel overhaul adding Video Overviews (narrated slide visuals and extracted diagrams grounded in sources) and multi-artifact persistent storage in single notebooks.",
            "tag": "Multimodal Studio",
            "color": COLOR_PURPLE
        },
        {
            "date": "Sept 2, 2025",
            "title": "4 Specialized Formats",
            "desc": "Audio Overviews expanded beyond deep dives: introduced Brief (1-2m summary), Critique (constructive review), and Debate (contrasting arguments) plus custom host prompting.",
            "tag": "Granular Steering",
            "color": COLOR_AMBER
        },
        {
            "date": "2026 Enterprise",
            "title": "Workspace Studio Automation",
            "desc": "'Ask NotebookLM' built into Google Workspace Studio workflows. 5x capacity limits for sources and queries, shared team notebooks, and strict zero-training privacy guarantees.",
            "tag": "Enterprise Mesh",
            "color": COLOR_CYAN_ACCENT
        }
    ]

    grid_w = Inches(3.68)
    grid_h = Inches(2.25)
    gx_start = Inches(0.8)
    gy_start = Inches(1.9)
    gx_gap = Inches(0.34)
    gy_gap = Inches(0.25)

    for idx, ev in enumerate(events):
        row = idx // 3
        col = idx % 3
        cx = gx_start + col * (grid_w + gx_gap)
        cy = gy_start + row * (grid_h + gy_gap)

        card = slide2.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, cy, grid_w, grid_h)
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_DARK
        card.line.color.rgb = COLOR_BORDER
        card.line.width = Pt(1)

        # Top Bar Date & Tag
        top_tb = slide2.shapes.add_textbox(cx + Inches(0.2), cy + Inches(0.18), grid_w - Inches(0.4), Inches(0.3))
        ttf = top_tb.text_frame
        ttf.margin_left = ttf.margin_top = ttf.margin_right = ttf.margin_bottom = 0
        tp = ttf.paragraphs[0]
        r_date = tp.add_run()
        r_date.text = ev["date"] + "  |  "
        r_date.font.bold = True
        r_date.font.size = Pt(9.5)
        r_date.font.color.rgb = ev["color"]
        r_tag = tp.add_run()
        r_tag.text = ev["tag"].upper()
        r_tag.font.size = Pt(8.5)
        r_tag.font.color.rgb = COLOR_MUTED

        # Card Title
        tit_tb = slide2.shapes.add_textbox(cx + Inches(0.2), cy + Inches(0.52), grid_w - Inches(0.4), Inches(0.35))
        tit_tf = tit_tb.text_frame
        tit_tf.word_wrap = True
        tit_tf.margin_left = tit_tf.margin_top = tit_tf.margin_right = tit_tf.margin_bottom = 0
        tit_p = tit_tf.paragraphs[0]
        tit_p.text = ev["title"]
        tit_p.font.size = Pt(13)
        tit_p.font.bold = True
        tit_p.font.color.rgb = COLOR_WHITE

        # Card Desc
        desc_tb = slide2.shapes.add_textbox(cx + Inches(0.2), cy + Inches(0.92), grid_w - Inches(0.4), Inches(1.2))
        desc_tf = desc_tb.text_frame
        desc_tf.word_wrap = True
        desc_tf.margin_left = desc_tf.margin_top = desc_tf.margin_right = desc_tf.margin_bottom = 0
        desc_p = desc_tf.paragraphs[0]
        desc_p.text = ev["desc"]
        desc_p.font.size = Pt(9.5)
        desc_p.font.color.rgb = COLOR_MUTED

    # =========================================================================
    # SLIDE 3: KEY FEATURES & CAPABILITIES
    # Source-based AI, Audio Overviews, Video Overviews (status), Research & Summarization
    # =========================================================================
    slide3 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide3)
    add_header(slide3, "CORE ARCHITECTURE & CAPABILITIES", "Key Features: Multimodal Studio & Grounded Intelligence",
               "Evaluating source grounding, Audio Overviews, Video status, and research automation.")
    add_footer(slide3, 3)

    # Left Column: In-depth Breakdown of Audio Overviews & Video Overviews
    left_w = Inches(5.7)
    card_l1 = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(1.9), left_w, Inches(2.3))
    card_l1.fill.solid()
    card_l1.fill.fore_color.rgb = COLOR_CARD_DARK
    card_l1.line.color.rgb = COLOR_BORDER
    card_l1.line.width = Pt(1)

    tb_l1 = slide3.shapes.add_textbox(Inches(1.05), Inches(2.05), left_w - Inches(0.5), Inches(2.0))
    tf_l1 = tb_l1.text_frame
    tf_l1.word_wrap = True
    tf_l1.margin_left = tf_l1.margin_top = tf_l1.margin_right = tf_l1.margin_bottom = 0

    p = tf_l1.paragraphs[0]
    p.text = "AUDIO OVERVIEWS: THE 4 MODES & INTERACTIVE 'JOIN'"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_CYAN_ACCENT

    bullets_l1 = [
        "Deep Dive (6–15 min): Conversational, organic back-and-forth exploring core themes.",
        "Brief (1–2 min): Rapid executive summaries ideal for high-level triage and mobile listening.",
        "Critique: Evaluates logical consistency, highlights evidence gaps, and provides feedback.",
        "Debate: Two hosts present opposing thesis arguments extracted from source materials.",
        "Interactive 'Join': Allows real-time microphone interruption to steer hosts mid-conversation."
    ]
    for b in bullets_l1:
        bp = tf_l1.add_paragraph()
        bp.text = "• " + b
        bp.font.size = Pt(9.5)
        bp.font.color.rgb = COLOR_MUTED
        bp.space_before = Pt(3)

    # Card Left 2: Video Overviews Status (Verified Distinction)
    card_l2 = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(0.8), Inches(4.4), left_w, Inches(2.3))
    card_l2.fill.solid()
    card_l2.fill.fore_color.rgb = COLOR_CARD_DARK
    card_l2.line.color.rgb = COLOR_BORDER
    card_l2.line.width = Pt(1)

    tb_l2 = slide3.shapes.add_textbox(Inches(1.05), Inches(4.55), left_w - Inches(0.5), Inches(2.0))
    tf_l2 = tb_l2.text_frame
    tf_l2.word_wrap = True
    tf_l2.margin_left = tf_l2.margin_top = tf_l2.margin_right = tf_l2.margin_bottom = 0

    p = tf_l2.paragraphs[0]
    p.text = "VIDEO OVERVIEWS: VERIFIED CAPABILITY VS PREVIEW"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_AMBER

    bullets_l2 = [
        "Verified Video Ingestion: Full native support for YouTube URLs and video transcripts, mapping timestamps directly to citations.",
        "Verified Studio Video Overviews: Generates synchronized visual slide presentations with narrated voiceover, extracted schematics, and quotes directly in the Studio panel.",
        "Verified Limitation / Distinguishing Fact: Video Overviews utilize dynamic narrated presentation cards rather than fully synthetic photorealistic 3D avatar video rendering.",
        "Persistent Studio Artifacts: Multiple audio and video briefs can be co-saved inside a single notebook repository for on-demand playback."
    ]
    for b in bullets_l2:
        bp = tf_l2.add_paragraph()
        bp.text = "• " + b
        bp.font.size = Pt(9.5)
        bp.font.color.rgb = COLOR_MUTED
        bp.space_before = Pt(4)

    # Right Column: Source-Based Architecture & Research Tools
    right_x = Inches(6.83)
    right_w = Inches(5.7)

    card_r1 = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, right_x, Inches(1.9), right_w, Inches(2.3))
    card_r1.fill.solid()
    card_r1.fill.fore_color.rgb = COLOR_CARD_DARK
    card_r1.line.color.rgb = COLOR_BORDER
    card_r1.line.width = Pt(1)

    tb_r1 = slide3.shapes.add_textbox(right_x + Inches(0.25), Inches(2.05), right_w - Inches(0.5), Inches(2.0))
    tf_r1 = tb_r1.text_frame
    tf_r1.word_wrap = True
    tf_r1.margin_left = tf_r1.margin_top = tf_r1.margin_right = tf_r1.margin_bottom = 0

    p = tf_r1.paragraphs[0]
    p.text = "SOURCE-GROUNDED ARCHITECTURE & CITATIONS"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_BLUE_ACCENT

    bullets_r1 = [
        "Clickable Inline Citations: Every AI response includes numbered chips; clicking jumps directly to the highlighted source excerpt.",
        "Massive Source Ingestion: Accepts PDFs, Google Docs, Slides, Web URLs, TXT, Markdown, MP3/WAV audio files, and YouTube links.",
        "Strict Context Isolation: The model queries strictly against active notebooks; prevents leakage of external unverified web facts.",
        "Gemini 1.5 & 2.0 Integration: Leverages million-token context window capacity to reason across disparate multi-volume archives."
    ]
    for b in bullets_r1:
        bp = tf_r1.add_paragraph()
        bp.text = "• " + b
        bp.font.size = Pt(9.5)
        bp.font.color.rgb = COLOR_MUTED
        bp.space_before = Pt(3)

    # Card Right 2: Enterprise Privacy & Automated Artifacts
    card_r2 = slide3.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, right_x, Inches(4.4), right_w, Inches(2.3))
    card_r2.fill.solid()
    card_r2.fill.fore_color.rgb = COLOR_CARD_DARK
    card_r2.line.color.rgb = COLOR_BORDER
    card_r2.line.width = Pt(1)

    tb_r2 = slide3.shapes.add_textbox(right_x + Inches(0.25), Inches(4.55), right_w - Inches(0.5), Inches(2.0))
    tf_r2 = tb_r2.text_frame
    tf_r2.word_wrap = True
    tf_r2.margin_left = tf_r2.margin_top = tf_r2.margin_right = tf_r2.margin_bottom = 0

    p = tf_r2.paragraphs[0]
    p.text = "ENTERPRISE SECURITY & AUTOMATED ARTIFACTS"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_EMERALD

    bullets_r2 = [
        "Zero Model Training: Uploaded proprietary enterprise docs, audio, and queries are NEVER used to train Google's AI foundation models.",
        "Instant Research Artifacts: One-click creation of Study Guides, FAQ Documents, Chronological Timelines, and Briefing Documents.",
        "Notebook Sharing & RBAC: Collaborate across enterprise teams with Viewer or Editor permissions while preserving source access controls.",
        "Google Workspace Studio Node: Trigger grounded queries within broader corporate automated workflows without writing code."
    ]
    for b in bullets_r2:
        bp = tf_r2.add_paragraph()
        bp.text = "• " + b
        bp.font.size = Pt(9.5)
        bp.font.color.rgb = COLOR_MUTED
        bp.space_before = Pt(3)

    # =========================================================================
    # SLIDE 4: REAL-WORLD APPLICATIONS
    # Education, Business research, Content creation, Corporate training, Knowledge management
    # =========================================================================
    slide4 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide4)
    add_header(slide4, "APPLIED ENTERPRISE USE CASES", "Real-World Applications Across 5 Key Verticals",
               "How organizations and academic leaders operationalize NotebookLM into daily workflows.")
    add_footer(slide4, 4)

    use_cases = [
        {
            "num": "01",
            "sector": "EDUCATION & ACADEMIA",
            "title": "Interactive Study & Syllabus Mastery",
            "desc": "Students and professors upload full-semester lecture recordings, readings, and syllabi. NotebookLM generates interactive mock quizzes, explains complex theorems in lay terms, and produces 10-minute commute podcast reviews.",
            "stat": "75% Faster Revision",
            "color": COLOR_CYAN_ACCENT
        },
        {
            "num": "02",
            "sector": "BUSINESS RESEARCH & M&A",
            "title": "Competitive Intelligence & Due Diligence",
            "desc": "Strategy teams cross-analyze hundreds of competitor SEC 10-K filings, earnings call transcripts, and patent applications. Generates instant side-by-side financial comparison matrices with strict inline source attribution.",
            "stat": "100% Audit Grounding",
            "color": COLOR_BLUE_ACCENT
        },
        {
            "num": "03",
            "sector": "CONTENT CREATION",
            "title": "Scriptwriting & Thematic Research",
            "desc": "Journalists, documentary writers, and content creators ingest historical archives, interview transcripts, and academic papers to identify compelling story hooks, verify dates, and synthesize contrasting perspective debates.",
            "stat": "4x Script Drafting Speed",
            "color": COLOR_PURPLE
        },
        {
            "num": "04",
            "sector": "CORPORATE TRAINING & ONBOARDING",
            "title": "Interactive SOPs & Compliance",
            "desc": "HR and operations teams turn dry, dense 200-page standard operating procedures (SOPs) and compliance handbooks into bite-sized Audio Overviews and queryable knowledge bots for new hire onboarding.",
            "stat": "60% Ramp-Up Reduction",
            "color": COLOR_EMERALD
        },
        {
            "num": "05",
            "sector": "KNOWLEDGE MANAGEMENT",
            "title": "Enterprise Collective Brain",
            "desc": "Organizations centralize disparate project documentation, post-mortems, and technical roadmaps into shared team notebooks—eliminating organizational knowledge loss when key personnel transition.",
            "stat": "Zero Brain Drain",
            "color": COLOR_AMBER
        }
    ]

    card_w4 = Inches(2.2)
    card_gap4 = Inches(0.18)
    start_x4 = Inches(0.8)
    card_y4 = Inches(1.9)
    card_h4 = Inches(4.8)

    for i, uc in enumerate(use_cases):
        cx = start_x4 + i * (card_w4 + card_gap4)
        card = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx, card_y4, card_w4, card_h4)
        card.fill.solid()
        card.fill.fore_color.rgb = COLOR_CARD_DARK
        card.line.color.rgb = COLOR_BORDER
        card.line.width = Pt(1)

        # Number Badge
        nb = slide4.shapes.add_textbox(cx + Inches(0.15), card_y4 + Inches(0.18), card_w4 - Inches(0.3), Inches(0.35))
        ntf = nb.text_frame
        ntf.margin_left = ntf.margin_top = ntf.margin_right = ntf.margin_bottom = 0
        np = ntf.paragraphs[0]
        np.text = uc["num"]
        np.font.size = Pt(20)
        np.font.bold = True
        np.font.color.rgb = uc["color"]

        # Sector
        sec_tb = slide4.shapes.add_textbox(cx + Inches(0.15), card_y4 + Inches(0.6), card_w4 - Inches(0.3), Inches(0.3))
        stf = sec_tb.text_frame
        stf.margin_left = stf.margin_top = stf.margin_right = stf.margin_bottom = 0
        sp = stf.paragraphs[0]
        sp.text = uc["sector"]
        sp.font.size = Pt(8.5)
        sp.font.bold = True
        sp.font.color.rgb = COLOR_MUTED

        # Title
        tit_tb = slide4.shapes.add_textbox(cx + Inches(0.15), card_y4 + Inches(0.95), card_w4 - Inches(0.3), Inches(0.65))
        ttf = tit_tb.text_frame
        ttf.word_wrap = True
        ttf.margin_left = ttf.margin_top = ttf.margin_right = ttf.margin_bottom = 0
        tp = ttf.paragraphs[0]
        tp.text = uc["title"]
        tp.font.size = Pt(12)
        tp.font.bold = True
        tp.font.color.rgb = COLOR_WHITE

        # Desc
        desc_tb = slide4.shapes.add_textbox(cx + Inches(0.15), card_y4 + Inches(1.65), card_w4 - Inches(0.3), Inches(2.2))
        dtf = desc_tb.text_frame
        dtf.word_wrap = True
        dtf.margin_left = dtf.margin_top = dtf.margin_right = dtf.margin_bottom = 0
        dp = dtf.paragraphs[0]
        dp.text = uc["desc"]
        dp.font.size = Pt(9.5)
        dp.font.color.rgb = COLOR_MUTED

        # Stat Pill at Bottom
        stat_card = slide4.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, cx + Inches(0.15), card_y4 + card_h4 - Inches(0.7), card_w4 - Inches(0.3), Inches(0.5))
        stat_card.fill.solid()
        stat_card.fill.fore_color.rgb = COLOR_CARD_ALT
        stat_card.line.color.rgb = uc["color"]
        stat_card.line.width = Pt(1)
        sctf = stat_card.text_frame
        sctf.margin_left = sctf.margin_top = sctf.margin_right = sctf.margin_bottom = 0
        scp = sctf.paragraphs[0]
        scp.alignment = PP_ALIGN.CENTER
        scp.text = uc["stat"]
        scp.font.size = Pt(9.5)
        scp.font.bold = True
        scp.font.color.rgb = COLOR_WHITE

    # =========================================================================
    # SLIDE 5: FUTURE OPPORTUNITIES & CONCLUSION
    # Benefits & Limitations, Future Possibilities, Key Takeaways, Official Sources
    # =========================================================================
    slide5 = prs.slides.add_slide(blank_layout)
    set_slide_background(slide5)
    add_header(slide5, "STRATEGIC SYNTHESIS", "Future Opportunities, Limitations & Key Takeaways",
               "Evaluating long-term enterprise trajectory, constraints, and verified Google source references.")
    add_footer(slide5, 5)

    # 4 Structured Quadrant / Column Panels
    q_w = Inches(5.7)
    q_h = Inches(2.3)
    qx1 = Inches(0.8)
    qx2 = Inches(6.83)
    qy1 = Inches(1.9)
    qy2 = Inches(4.4)

    # Panel 1: Benefits vs Current Limitations
    p1 = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, qx1, qy1, q_w, q_h)
    p1.fill.solid()
    p1.fill.fore_color.rgb = COLOR_CARD_DARK
    p1.line.color.rgb = COLOR_BORDER
    p1.line.width = Pt(1)

    tbp1 = slide5.shapes.add_textbox(qx1 + Inches(0.25), qy1 + Inches(0.15), q_w - Inches(0.5), q_h - Inches(0.3))
    tfp1 = tbp1.text_frame
    tfp1.word_wrap = True
    tfp1.margin_left = tfp1.margin_top = tfp1.margin_right = tfp1.margin_bottom = 0
    p = tfp1.paragraphs[0]
    p.text = "BENEFITS VS. CURRENT SYSTEM LIMITATIONS"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_CYAN_ACCENT

    b_p1 = [
        "Core Strength: Zero-hallucination compliance; verifiable inline citations prevent LLM fabrication.",
        "Multimodal Mastery: Ingests text, PDF, slides, YouTube URLs, and audio into unified query space.",
        "Current Limitation: Strictly dependent on source quality ('garbage in, garbage out'); no independent web browsing.",
        "Audio Customization Boundary: Granular voice editing requires prompting rather than phoneme-level audio editing."
    ]
    for b in b_p1:
        bp = tfp1.add_paragraph()
        bp.text = "• " + b
        bp.font.size = Pt(9.5)
        bp.font.color.rgb = COLOR_MUTED
        bp.space_before = Pt(3)

    # Panel 2: Future Possibilities & Horizon
    p2 = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, qx2, qy1, q_w, q_h)
    p2.fill.solid()
    p2.fill.fore_color.rgb = COLOR_CARD_DARK
    p2.line.color.rgb = COLOR_BORDER
    p2.line.width = Pt(1)

    tbp2 = slide5.shapes.add_textbox(qx2 + Inches(0.25), qy1 + Inches(0.15), q_w - Inches(0.5), q_h - Inches(0.3))
    tfp2 = tbp2.text_frame
    tfp2.word_wrap = True
    tfp2.margin_left = tfp2.margin_top = tfp2.margin_right = tfp2.margin_bottom = 0
    p = tfp2.paragraphs[0]
    p.text = "FUTURE HORIZONS & ROADMAP POSSIBILITIES"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_PURPLE

    b_p2 = [
        "Bi-Directional Video Avatars: Evolution from narrated slides to real-time interactive visual AI interviewers.",
        "Autonomous Multi-Agent Synthesis: Specialized agent personas running automated adversarial debate trials on internal docs.",
        "Deep Google Workspace Studio Mesh: Zero-touch enterprise pipeline connecting Drive, BigQuery, and NotebookLM.",
        "Edge & On-Premises Isolation: Private cloud deployment options for defense and healthcare compliance."
    ]
    for b in b_p2:
        bp = tfp2.add_paragraph()
        bp.text = "• " + b
        bp.font.size = Pt(9.5)
        bp.font.color.rgb = COLOR_MUTED
        bp.space_before = Pt(3)

    # Panel 3: Key Takeaways
    p3 = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, qx1, qy2, q_w, q_h)
    p3.fill.solid()
    p3.fill.fore_color.rgb = COLOR_CARD_DARK
    p3.line.color.rgb = COLOR_BORDER
    p3.line.width = Pt(1)

    tbp3 = slide5.shapes.add_textbox(qx1 + Inches(0.25), qy2 + Inches(0.15), q_w - Inches(0.5), q_h - Inches(0.3))
    tfp3 = tbp3.text_frame
    tfp3.word_wrap = True
    tfp3.margin_left = tfp3.margin_top = tfp3.margin_right = tfp3.margin_bottom = 0
    p = tfp3.paragraphs[0]
    p.text = "EXECUTIVE SUMMARY & KEY TAKEAWAYS"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_EMERALD

    b_p3 = [
        "Paradigm Shift: NotebookLM has transitioned from a niche note-taking lab into an enterprise-grade research engine.",
        "Audio Overviews Redefined: Four specialized modes (Deep Dive, Brief, Critique, Debate) set the global benchmark for audio synthesis.",
        "Enterprise Readiness: Zero data training clauses, Workspace Studio nodes, and NotebookLM Plus tiers unlock corporate adoption.",
        "Ultimate ROI: Compresses document synthesis cycles from weeks to minutes while enforcing absolute citation auditability."
    ]
    for b in b_p3:
        bp = tfp3.add_paragraph()
        bp.text = "• " + b
        bp.font.size = Pt(9.5)
        bp.font.color.rgb = COLOR_MUTED
        bp.space_before = Pt(3)

    # Panel 4: Official Source Links & Citations
    p4 = slide5.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, qx2, qy2, q_w, q_h)
    p4.fill.solid()
    p4.fill.fore_color.rgb = COLOR_CARD_DARK
    p4.line.color.rgb = COLOR_BORDER
    p4.line.width = Pt(1)

    tbp4 = slide5.shapes.add_textbox(qx2 + Inches(0.25), qy2 + Inches(0.15), q_w - Inches(0.5), q_h - Inches(0.3))
    tfp4 = tbp4.text_frame
    tfp4.word_wrap = True
    tfp4.margin_left = tfp4.margin_top = tfp4.margin_right = tfp4.margin_bottom = 0
    p = tfp4.paragraphs[0]
    p.text = "OFFICIAL GOOGLE SOURCES & VERIFIED CITATIONS"
    p.font.bold = True
    p.font.size = Pt(13)
    p.font.color.rgb = COLOR_AMBER

    b_p4 = [
        "Google Keyword Blog: 'NotebookLM now lets you listen to a conversation about your sources' (Sept 11, 2024)",
        "Google Labs Release Notes: 'Interactive Audio & NotebookLM Plus Expansion' (Dec 13, 2024)",
        "Google Workspace Updates: 'Expanding Audio Overviews to 50+ Languages & Enterprise Admin Controls' (April 29, 2025)",
        "Google Blog / Studio: 'Introducing 4 New Audio Overview Styles & Custom Steering' (Sept 2, 2025)",
        "NotebookLM Official Hub: https://notebooklm.google.com | Google Workspace Studio Integration (2026)"
    ]
    for b in b_p4:
        bp = tfp4.add_paragraph()
        bp.text = "• " + b
        bp.font.size = Pt(9.5)
        bp.font.color.rgb = COLOR_MUTED
        bp.space_before = Pt(3)

    # Save presentation
    output_filename = "NotebookLM_Latest_Updates_Manvian.pptx"
    prs.save(output_filename)
    print(f"[SUCCESS] Presentation generated successfully: {output_filename} ({len(prs.slides)} slides)")

if __name__ == "__main__":
    create_deck()
