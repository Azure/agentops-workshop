#!/usr/bin/env python3
"""Render the code-based diagrams for the short AgentOps deck.

Output style matches the upstream presentations/04-agentops/images/ aesthetic:
    - white background
    - navy title (#003366) in Segoe UI Semibold (or fallback)
    - rounded rectangles with white text in MS Office palette
    - subtle thin connectors between blocks

Usage:
    python make_diagrams.py [name1 name2 ...]
    python make_diagrams.py all
    python make_diagrams.py --no-header all

Flags:
    --no-header   Omit the title and subtitle text from diagrams
                  (useful when the slide already has its own heading).
"""

from __future__ import annotations

import math
import os
import sys
from pathlib import Path

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Polygon
from matplotlib.patches import Rectangle, ConnectionPatch
import matplotlib.font_manager as fm

# ---------------------------------------------------------------------------
# Style constants
# ---------------------------------------------------------------------------
NAVY    = "#003366"
BLUE    = "#0078D4"
TEAL    = "#117865"
ORANGE  = "#D83B01"
PURPLE  = "#5C2D91"
GREEN   = "#107C10"
GOLD    = "#B27D00"
GRAY    = "#6B6B6B"
LIGHT   = "#F2F2F2"
WHITE   = "#FFFFFF"
TEXT_DK = "#111827"

# Resolve a usable font: Segoe UI on Windows, fallback to DejaVu Sans.
_FONTS = {f.name for f in fm.fontManager.ttflist}
HEADING_FONT = "Segoe UI Semibold" if "Segoe UI Semibold" in _FONTS else (
    "Segoe UI" if "Segoe UI" in _FONTS else "DejaVu Sans"
)
BODY_FONT = "Segoe UI" if "Segoe UI" in _FONTS else "DejaVu Sans"

REPO_ROOT = Path(__file__).resolve().parent.parent.parent
OUT_DIR = REPO_ROOT / "short" / "images"
OUT_DIR.mkdir(parents=True, exist_ok=True)

DPI = 200
W, H = 16, 9  # inches; 16:9

# Global flag: when True, add_title() and add_subtitle() become no-ops.
SHOW_HEADER = True


# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------
def new_canvas():
    h = H if SHOW_HEADER else H * 0.82  # Shorter canvas when no title
    ylim_top = 56.25 if SHOW_HEADER else 46
    fig, ax = plt.subplots(figsize=(W, h), dpi=DPI, facecolor=WHITE)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, ylim_top)
    ax.set_aspect("equal")
    ax.set_axis_off()
    return fig, ax


def add_title(ax, text, y=51, color=NAVY, size=26):
    if not SHOW_HEADER:
        # Small semi-transparent reference in the bottom-right corner
        ax.text(96, 3, text, ha="right", va="bottom", color=NAVY,
                fontsize=8, fontfamily=BODY_FONT, alpha=0.3)
        return
    ax.text(50, y, text, ha="center", va="center", color=color,
            fontsize=size, fontfamily=HEADING_FONT, fontweight="bold")


def add_subtitle(ax, text, y=47, color=GRAY, size=14):
    if not SHOW_HEADER:
        return
    ax.text(50, y, text, ha="center", va="center", color=color,
            fontsize=size, fontfamily=BODY_FONT)


def rounded_box(ax, x, y, w, h, color, text="", text_color=WHITE,
                text_size=14, bold=True, radius=1.2):
    box = FancyBboxPatch(
        (x, y), w, h,
        boxstyle=f"round,pad=0.0,rounding_size={radius}",
        linewidth=0, facecolor=color, edgecolor="none",
    )
    ax.add_patch(box)
    if text:
        ax.text(x + w / 2, y + h / 2, text,
                ha="center", va="center",
                color=text_color, fontsize=text_size,
                fontfamily=HEADING_FONT if bold else BODY_FONT,
                fontweight="bold" if bold else "normal")


def text_block(ax, x, y, lines, size=11, color=TEXT_DK, va="top",
               ha="center", line_h=2.0):
    if isinstance(lines, str):
        lines = [lines]
    for i, ln in enumerate(lines):
        ax.text(x, y - i * line_h, ln, ha=ha, va=va, color=color,
                fontsize=size, fontfamily=BODY_FONT)


def save(fig, name):
    path = OUT_DIR / name
    fig.savefig(path, dpi=DPI, bbox_inches="tight", facecolor=WHITE,
                edgecolor="none", pad_inches=0.3)
    plt.close(fig)
    print(f"  saved: {path}  ({path.stat().st_size:,} bytes)")


# ---------------------------------------------------------------------------
# Diagram: complexity ladder (5 rungs)
# ---------------------------------------------------------------------------
def complexity_ladder():
    fig, ax = new_canvas()
    add_title(ax, "Complexity grows from prompts to agents")
    add_subtitle(ax, "Each rung adds new operational surface area to monitor and govern")

    rungs = [
        ("Prompts",        BLUE,   "Single prompt, single model.\nDeterministic, easy to test."),
        ("RAG",            TEAL,   "Adds retrieval, grounding,\nvector DB ops, dataset drift."),
        ("Tools",          GREEN,  "Adds function calling,\nside effects, auth boundaries."),
        ("Single agent",   ORANGE, "Adds planning, memory,\nmulti-step traces, escalation."),
        ("Multi-agent",    PURPLE, "Adds orchestration,\nemergent behaviour, cost spikes."),
    ]
    n = len(rungs)
    base_x = 6
    step_x = (100 - 2 * base_x) / n
    box_w = step_x * 0.85
    box_h = 5
    for i, (label, color, body) in enumerate(rungs):
        x = base_x + i * step_x + (step_x - box_w) / 2
        y = 10 + i * 5  # rising staircase
        rounded_box(ax, x, y, box_w, box_h, color, label, text_size=15)
        # body text below the rung
        text_block(ax, x + box_w / 2, y - 0.8,
                   body.split("\n"), size=10, color=TEXT_DK, va="top",
                   ha="center", line_h=1.6)

    # Diagonal arrow showing growth
    ax.annotate("",
                xy=(95, 40), xytext=(5, 8),
                arrowprops=dict(arrowstyle="-", color=GRAY, lw=1, alpha=0.4,
                                linestyle=(0, (4, 4))))
    ax.text(95, 41, "operational\ncomplexity", ha="right", va="bottom",
            color=GRAY, fontsize=10, fontfamily=BODY_FONT, style="italic")
    save(fig, "complexity-ladder.png")


# ---------------------------------------------------------------------------
# Diagram: 6-step operating loop
# ---------------------------------------------------------------------------
def operating_loop():
    fig, ax = new_canvas()
    add_title(ax, "AgentOps operating model: a 6-step loop")
    add_subtitle(ax, "Foundry stays the control plane. AgentOps connects signals to release decisions.")

    steps = [
        ("Evaluate", BLUE,   "Pre-prod scoring on golden datasets,\nquality + safety + agent metrics."),
        ("Gate",     TEAL,   "CI/CD policy thresholds, human approval,\nartefact promotion across envs."),
        ("Observe",  GREEN,  "Traces, metrics, logs, content safety\nflows into Foundry + App Insights."),
        ("Diagnose", GOLD,   "Root cause via traces, evaluators on\nproduction samples, KQL queries."),
        ("Ship",     ORANGE, "Canary rollouts, model + prompt + tool\nversioned and deployed together."),
        ("Improve",  PURPLE, "Feedback into the dataset, evaluators,\nfine-tuning, prompt revisions."),
    ]
    cx, cy = 50, 22
    r = 11
    text_r = 19
    n = len(steps)
    # Start at top (12 o'clock) and go clockwise
    for i, (label, color, body) in enumerate(steps):
        angle = math.pi / 2 - i * (2 * math.pi / n)
        x = cx + r * math.cos(angle)
        y = cy + r * math.sin(angle)
        box_w, box_h = 12, 4
        rounded_box(ax, x - box_w / 2, y - box_h / 2, box_w, box_h, color,
                    label, text_size=14)
        # Body text - placed well outside the circle so nothing overlaps the wheel
        tx = cx + text_r * math.cos(angle)
        ty = cy + text_r * math.sin(angle)
        # Convert angle to compass direction for alignment
        cos_a = math.cos(angle)
        sin_a = math.sin(angle)
        if cos_a > 0.5:
            ha = "left"
            tx += 1.5
        elif cos_a < -0.5:
            ha = "right"
            tx -= 1.5
        else:
            ha = "center"
        if sin_a > 0.5:
            va = "bottom"
            ty += 1.5
        elif sin_a < -0.5:
            va = "top"
            ty -= 1.5
        else:
            va = "center"
        ax.text(tx, ty, body, ha=ha, va=va, color=TEXT_DK,
                fontsize=10, fontfamily=BODY_FONT, linespacing=1.3)

    # Connectors between adjacent nodes (curved arrows between edges of nodes)
    for i in range(n):
        a1 = math.pi / 2 - i * (2 * math.pi / n)
        a2 = math.pi / 2 - ((i + 1) % n) * (2 * math.pi / n)
        # Start/end near edge of current and next nodes along the circle
        # Use a slightly smaller radius so arrow heads don't overlap the boxes
        rr = r - 0.5
        # Offset start/end by ~0.45 of node angular width so arrows live in the gap
        gap = 2 * math.pi / n * 0.28
        x1 = cx + rr * math.cos(a1 - gap)
        y1 = cy + rr * math.sin(a1 - gap)
        x2 = cx + rr * math.cos(a2 + gap)
        y2 = cy + rr * math.sin(a2 + gap)
        arrow = FancyArrowPatch((x1, y1), (x2, y2),
                                connectionstyle="arc3,rad=-0.3",
                                arrowstyle="-|>", mutation_scale=14,
                                color=GRAY, lw=1.4, alpha=0.7)
        ax.add_patch(arrow)

    save(fig, "operating-loop.png")


# ---------------------------------------------------------------------------
# Diagram: four-pillar operating model (Evaluate -> Ship -> Observe -> Own)
# ---------------------------------------------------------------------------
def four_pillars():
    fig, ax = new_canvas()
    add_title(ax, "AgentOps operating model: four pillars")
    add_subtitle(ax, "Evaluate, ship, observe, and own production agents. Foundry stays the control plane.")

    pillars = [
        ("Evaluate", BLUE,
         ["datasets", "rubrics", "red teaming", "thresholds"]),
        ("Ship", TEAL,
         ["gates", "approvals", "release evidence", "canary"]),
        ("Observe", GREEN,
         ["traces", "metrics", "feedback", "correlation"]),
        ("Own", ORANGE,
         ["diagnose", "runbooks", "improve", "model lifecycle"]),
    ]

    n = len(pillars)
    box_w = 18
    gap = 4
    total = n * box_w + (n - 1) * gap
    x0 = (100 - total) / 2
    head_y = 35
    head_h = 7
    card_y = 9
    card_h = 24

    for i, (label, color, practices) in enumerate(pillars):
        x = x0 + i * (box_w + gap)
        cx = x + box_w / 2

        # Light practice card behind the examples
        rounded_box(ax, x, card_y, box_w, card_h, LIGHT, radius=1.2)
        # Pillar header box
        rounded_box(ax, x, head_y, box_w, head_h, color, label, text_size=18)

        # Practice examples stacked inside the card
        py = card_y + card_h - 4
        for p in practices:
            ax.text(cx, py, p, ha="center", va="center", color=TEXT_DK,
                    fontsize=12, fontfamily=BODY_FONT)
            py -= 5.2

        # Arrow to the next pillar
        if i < n - 1:
            ax1 = x + box_w + 0.4
            ax2 = x + box_w + gap - 0.4
            arrow = FancyArrowPatch((ax1, head_y + head_h / 2),
                                    (ax2, head_y + head_h / 2),
                                    arrowstyle="-|>", mutation_scale=18,
                                    color=GRAY, lw=2.0)
            ax.add_patch(arrow)

    # Feedback connector: Own loops back to Evaluate (dashed, flat, below cards)
    lx1 = x0 + (n - 1) * (box_w + gap) + box_w / 2
    lx2 = x0 + box_w / 2
    feedback = FancyArrowPatch((lx1, card_y - 1), (lx2, card_y - 1),
                               connectionstyle="arc3,rad=-0.05",
                               arrowstyle="-|>", mutation_scale=16,
                               color=GRAY, lw=1.4, ls="--", alpha=0.7)
    ax.add_patch(feedback)
    ax.text((lx1 + lx2) / 2, card_y - 5,
            "production learnings feed the next cycle",
            ha="center", va="top", color=GRAY, fontsize=10,
            fontfamily=BODY_FONT, style="italic")

    save(fig, "agentops-four-pillars.png")


# ---------------------------------------------------------------------------
# Diagram: maturity ribbon (4 levels)
# ---------------------------------------------------------------------------
def maturity_ribbon():
    fig, ax = new_canvas()
    add_title(ax, "AgentOps maturity model")
    add_subtitle(ax, "Where is your team today? Pick the next adjacent level, not the destination.")

    levels = [
        ("1", "Initial", BLUE,
         "Ad hoc demos.\nManual eval, no gates.\nLogs scattered."),
        ("2", "Defined", TEAL,
         "Versioned prompts + agents.\nPre-prod eval datasets.\nCI builds artefacts."),
        ("3", "Managed", GREEN,
         "Quality + safety gates in CI.\nContinuous eval in prod.\nRunbooks + SLOs."),
        ("4", "Optimised", PURPLE,
         "Drift + cost guardrails.\nCanary + auto-rollback.\nFeedback flywheel."),
    ]
    base_x = 4
    avail = 92
    n = len(levels)
    box_w = avail / n - 2
    box_h = 8
    y = 26
    for i, (idx, label, color, body) in enumerate(levels):
        x = base_x + i * (avail / n)
        # Big numbered header
        rounded_box(ax, x, y + 5, box_w, 4.5, color, f"Level {idx} - {label}",
                    text_size=15, radius=1.0)
        # Body
        rounded_box(ax, x, y - 6.5, box_w, 10.5, LIGHT, "",
                    text_color=TEXT_DK, radius=1.0)
        # Body text
        body_lines = body.split("\n")
        for j, ln in enumerate(body_lines):
            ax.text(x + box_w / 2, y - 0.3 - j * 1.8, ln,
                    ha="center", va="center", color=TEXT_DK,
                    fontsize=11, fontfamily=BODY_FONT)
        # Arrow between cards
        if i < n - 1:
            arrow_x = x + box_w + 0.3
            arrow_x2 = x + (avail / n) - 0.3
            arrow = FancyArrowPatch((arrow_x, y + 7), (arrow_x2, y + 7),
                                    arrowstyle="-|>", mutation_scale=15,
                                    color=GRAY, lw=1.6)
            ax.add_patch(arrow)
    save(fig, "maturity-ribbon.png")


# ---------------------------------------------------------------------------
# Diagram: Foundry control plane (3 layers)
# ---------------------------------------------------------------------------
def foundry_control_plane():
    fig, ax = new_canvas()
    add_title(ax, "Microsoft Foundry is the AgentOps control plane")
    add_subtitle(ax, "Build, evaluate, deploy, observe - the same surfaces an SRE expects, adapted for agents.")

    # Three horizontal bands
    bands = [
        ("Surfaces", BLUE,
         ["Foundry portal", "Foundry SDK", "Azure CLI / REST", "GitHub Actions"]),
        ("Capabilities", TEAL,
         ["Agents + versions", "Quality + safety evaluators",
          "Agent evaluators", "Red Teaming agent",
          "OpenTelemetry tracing", "Content Safety"]),
        ("Runtime", PURPLE,
         ["Azure AI projects", "Model deployments",
          "Tool / MCP servers", "App Insights + Log Analytics"]),
    ]
    y_top = 38
    band_h = 7.5
    gap = 2
    label_x = 4
    label_w = 14
    pills_x0 = label_x + label_w + 2
    pills_x1 = 96
    pills_w = pills_x1 - pills_x0
    for i, (label, color, items) in enumerate(bands):
        y = y_top - i * (band_h + gap)
        # Header label on left
        rounded_box(ax, label_x, y, label_w, band_h, color, label, text_size=15)
        n = len(items)
        # Even distribution of pills with a small gap between them
        pill_gap = 1.2
        pill_w = (pills_w - pill_gap * (n - 1)) / n
        for j, it in enumerate(items):
            px = pills_x0 + j * (pill_w + pill_gap)
            # Pill background (white) + colored outline
            outline = FancyBboxPatch(
                (px, y + 0.6), pill_w, band_h - 1.2,
                boxstyle="round,pad=0.0,rounding_size=0.6",
                linewidth=1.4, facecolor=WHITE, edgecolor=color,
            )
            ax.add_patch(outline)
            ax.text(px + pill_w / 2, y + band_h / 2, it,
                    ha="center", va="center", color=TEXT_DK,
                    fontsize=10.5, fontfamily=BODY_FONT)

    # Bottom strip: where AgentOps adds value
    rounded_box(ax, 4, 5, 92, 5, NAVY,
                "AgentOps wires evaluators -> gates -> traces -> alerts -> rollouts back into the same control plane",
                text_size=12.5, bold=False, radius=1.0)

    save(fig, "foundry-control-plane.png")


# ---------------------------------------------------------------------------
# Diagram: telemetry to action (trace waterfall -> evaluator -> action)
# ---------------------------------------------------------------------------
def telemetry_to_action():
    fig, ax = new_canvas()
    add_title(ax, "From telemetry to action")
    add_subtitle(ax, "A single agent request becomes a trace, a metric, an alert, and an evaluator score.")

    # Left: trace waterfall
    bars = [
        ("agent.invoke",     0,  30, BLUE),
        ("plan",             2,  10, BLUE),
        ("tool.search",     12,  6, TEAL),
        ("tool.lookup",     18,  4, TEAL),
        ("model.completion",22,  6, PURPLE),
        ("emit response",   28,  2, GRAY),
    ]
    base_x = 4
    base_y = 30
    bar_h = 1.8
    scale = 1.5
    ax.text(base_x, base_y + 9, "Trace (App Insights)",
            ha="left", va="bottom", color=NAVY, fontsize=14,
            fontfamily=HEADING_FONT, fontweight="bold")
    for i, (label, start, dur, color) in enumerate(bars):
        y = base_y + 7 - i * (bar_h + 0.6)
        x = base_x + start * scale
        w = dur * scale
        rounded_box(ax, x, y, w, bar_h, color, "", radius=0.4)
        ax.text(base_x - 0.5, y + bar_h / 2, label, ha="right", va="center",
                color=TEXT_DK, fontsize=10, fontfamily=BODY_FONT)
        ax.text(x + w + 0.5, y + bar_h / 2, f"{dur*10}ms",
                ha="left", va="center", color=GRAY, fontsize=9,
                fontfamily=BODY_FONT)

    # Vertical separator
    ax.plot([55, 55], [10, 40], color=LIGHT, lw=2)

    # Right column: signals -> actions funnel
    ax.text(78, 39, "Signals  ->  Actions",
            ha="center", va="bottom", color=NAVY, fontsize=14,
            fontfamily=HEADING_FONT, fontweight="bold")
    rows = [
        ("Latency spike",      "Azure Monitor alert -> on-call",       ORANGE),
        ("Tool error rate",    "Disable tool, fall back to manual",    ORANGE),
        ("Safety violation",   "Block + content safety incident",      "#B91C1C"),
        ("Eval score drop",    "Pause canary, open ticket",            GOLD),
        ("Cost anomaly",       "Throttle via APIM, notify FinOps",     PURPLE),
        ("Positive feedback",  "Sample into eval dataset",             GREEN),
    ]
    rx = 58
    rw = 38
    rh = 3.6
    for i, (signal, action, color) in enumerate(rows):
        y = 35 - i * 4.2
        rounded_box(ax, rx, y, 14, rh, color, signal,
                    text_size=10.5, radius=0.6)
        rounded_box(ax, rx + 15, y, rw - 15, rh, LIGHT, action,
                    text_color=TEXT_DK, text_size=10.5, bold=False, radius=0.6)

    save(fig, "telemetry-to-action.png")


# ---------------------------------------------------------------------------
# Diagram: Red teaming taxonomy
# ---------------------------------------------------------------------------
def red_teaming_taxonomy():
    fig, ax = new_canvas()
    add_title(ax, "Red teaming and AI safety")
    add_subtitle(ax, "Foundry's Red Teaming agent automates adversarial probing across four risk categories.")

    cats = [
        ("Harmful content", "#B91C1C",
         "Hate, violence, sexual,\nself-harm. Content Safety\nclassifiers + custom probes."),
        ("Jailbreak",       ORANGE,
         "Prompt injection, role\nhijacking, system prompt\nleakage attempts."),
        ("Hallucination",   GOLD,
         "Ungrounded claims, fake\ncitations, false tool args.\nGroundedness evaluator."),
        ("Data exfiltration", PURPLE,
         "Sensitive data echo, tool\nabuse to read forbidden\nstores, PII leakage."),
    ]
    base_x = 6
    base_y = 18
    box_w = 21
    box_h = 22
    gap = 1.0
    for i, (label, color, body) in enumerate(cats):
        x = base_x + i * (box_w + gap)
        # Header band
        rounded_box(ax, x, base_y + box_h - 5, box_w, 5, color, label,
                    text_size=14, radius=1.0)
        # Body card
        rounded_box(ax, x, base_y, box_w, box_h - 5.4, LIGHT, "", radius=1.0)
        body_lines = body.split("\n")
        for j, ln in enumerate(body_lines):
            ax.text(x + box_w / 2, base_y + box_h - 8.5 - j * 2.2, ln,
                    ha="center", va="center", color=TEXT_DK,
                    fontsize=11, fontfamily=BODY_FONT)

    # Bottom band: process flow
    flow = ["Define risk profile", "Run automated probes",
            "Score + triage findings", "Fix + re-test in CI"]
    fy = 9
    fw_total = 92
    fw_each = fw_total / len(flow) - 2
    fx0 = 4
    for i, step in enumerate(flow):
        x = fx0 + i * (fw_total / len(flow))
        rounded_box(ax, x, fy, fw_each, 4, NAVY, step,
                    text_size=11, bold=False, radius=0.8)
        if i < len(flow) - 1:
            arrow = FancyArrowPatch((x + fw_each + 0.2, fy + 2),
                                    (x + fw_total / len(flow) - 0.2, fy + 2),
                                    arrowstyle="-|>", mutation_scale=12,
                                    color=GRAY, lw=1.4)
            ax.add_patch(arrow)
    save(fig, "red-teaming-taxonomy.png")


# ---------------------------------------------------------------------------
# Diagram: Day-2 four concerns (2x2 quadrant)
# ---------------------------------------------------------------------------
def day2_quadrant():
    fig, ax = new_canvas()
    add_title(ax, "Day-2 operations: four concerns")
    add_subtitle(ax, "What changes after you ship the first production agent")

    quads = [
        # (label, color, x, y, bullets)
        ("Reliability + SLOs", BLUE, 8, 25,
         ["Availability, latency, error rate budgets",
          "Tool dependency failure modes",
          "Graceful degradation"]),
        ("Incident response", ORANGE, 52, 25,
         ["Runbooks per severity",
          "On-call rotation that knows the agent",
          "Postmortems with model + prompt context"]),
        ("Model lifecycle", PURPLE, 8, 4,
         ["Canary rollout for model upgrades",
          "Prompt + tool versioned alongside model",
          "Rollback drills"]),
        ("Cost + capacity", TEAL, 52, 4,
         ["PTU vs pay-as-you-go decisions",
          "Token + tool call budgets per tenant",
          "Alerting on cost anomalies"]),
    ]
    qw, qh = 40, 18
    for label, color, x, y, items in quads:
        # Header bar
        rounded_box(ax, x, y + qh - 4, qw, 4, color, label,
                    text_size=14, radius=1.0)
        # Body
        rounded_box(ax, x, y, qw, qh - 4.2, LIGHT, "", radius=1.0)
        for j, it in enumerate(items):
            ax.text(x + 2, y + qh - 7 - j * 2.6, f"-  {it}",
                    ha="left", va="center", color=TEXT_DK,
                    fontsize=11.5, fontfamily=BODY_FONT)
    save(fig, "day2-quadrant.png")


# ---------------------------------------------------------------------------
# Diagram: anatomy + complexity combined (progressive table)
# ---------------------------------------------------------------------------
def anatomy_complexity():
    fig, ax = new_canvas()
    add_title(ax, "Building blocks of a production agent")
    add_subtitle(ax, "Each tier adds components and operational surface. A production agent manages all of these.")

    tiers = [
        ("Prompts",       BLUE,   "System prompt, model",
         "Versioning, quality eval, cost"),
        ("+ RAG",         TEAL,   "+ Knowledge sources, vector DB",
         "Freshness, permissions, groundedness"),
        ("+ Tools",       GREEN,  "+ Tool / MCP servers, guardrails",
         "Auth boundaries, side effects, failure modes"),
        ("+ Agent",       ORANGE, "+ Memory, orchestration, approval points",
         "Multi-step traces, loop prevention, escalation"),
        ("+ Multi-agent", PURPLE, "+ Orchestrator, sub-agents",
         "Emergent behaviour, coordination, cost spikes"),
    ]

    # Layout constants
    n = len(tiers)
    table_x = 4
    table_w = 92
    row_h = 5.0
    gap = 1.0
    # Position rows so they start well below the column headers
    top_y = 32
    # Column widths (proportional)
    col1_w = 16   # Tier label
    col2_w = 36   # Components
    col3_w = table_w - col1_w - col2_w - 4  # Operational surface
    col1_x = table_x
    col2_x = col1_x + col1_w + 2
    col3_x = col2_x + col2_w + 2

    # Column headers — placed above the first row with clear separation
    header_y = top_y + row_h + 2.5
    ax.text(col1_x + col1_w / 2, header_y, "Complexity tier",
            ha="center", va="center", color=NAVY, fontsize=13,
            fontfamily=HEADING_FONT, fontweight="bold")
    ax.text(col2_x + col2_w / 2, header_y, "Components in play",
            ha="center", va="center", color=NAVY, fontsize=13,
            fontfamily=HEADING_FONT, fontweight="bold")
    ax.text(col3_x + col3_w / 2, header_y, "New operational surface",
            ha="center", va="center", color=NAVY, fontsize=13,
            fontfamily=HEADING_FONT, fontweight="bold")

    for i, (tier, color, components, surface) in enumerate(tiers):
        y = top_y - i * (row_h + gap)
        # Tier label (colored rounded box)
        rounded_box(ax, col1_x, y, col1_w, row_h, color, tier,
                    text_size=13, radius=0.8)
        # Components (light background)
        rounded_box(ax, col2_x, y, col2_w, row_h, LIGHT, "", radius=0.8)
        ax.text(col2_x + col2_w / 2, y + row_h / 2, components,
                ha="center", va="center", color=TEXT_DK,
                fontsize=11.5, fontfamily=BODY_FONT)
        # Operational surface (light background)
        rounded_box(ax, col3_x, y, col3_w, row_h, LIGHT, "", radius=0.8)
        ax.text(col3_x + col3_w / 2, y + row_h / 2, surface,
                ha="center", va="center", color=TEXT_DK,
                fontsize=11.5, fontfamily=BODY_FONT)

    # Accumulation arrow on the left margin
    arrow_x = 2.5
    arrow_top = top_y + row_h / 2
    arrow_bot = top_y - (n - 1) * (row_h + gap) + row_h / 2
    arrow = FancyArrowPatch((arrow_x, arrow_top), (arrow_x, arrow_bot),
                            arrowstyle="-|>", mutation_scale=16,
                            color=GRAY, lw=2, alpha=0.5)
    ax.add_patch(arrow)

    # Bottom call-out
    rounded_box(ax, 4, 3, 92, 4.5, NAVY,
                "Every component is a versioned asset, an evaluation target, and an operational dependency.",
                text_size=12, bold=False, radius=1.0)

    save(fig, "anatomy-complexity.png")


# ---------------------------------------------------------------------------
# Diagram: production gap (two-column contrast)
# ---------------------------------------------------------------------------
def production_gap():
    fig, ax = new_canvas()
    add_title(ax, "The production gap")
    add_subtitle(ax, "The bottleneck moved from building the first demo to proving the next version is safe to release.")

    rows = [
        ("One happy-path demo",       "Repeatable evaluation across many cases"),
        ("Manual quality check",      "Release evidence and gates"),
        ("Single-version snapshot",   "Versioned models, prompts, and tools"),
        ("\"It looked good last week\"", "Trace-backed Day-2 operations"),
    ]

    # Layout
    n = len(rows)
    col_gap = 6
    col_w = 40
    row_h = 5.5
    gap = 1.5
    left_x = 4
    right_x = left_x + col_w + col_gap
    top_y = 33

    # Column headers
    header_y = top_y + row_h + 2.0
    rounded_box(ax, left_x, header_y - 1.5, col_w, 4, GRAY,
                "Prototype works", text_size=15, radius=1.0)
    rounded_box(ax, right_x, header_y - 1.5, col_w, 4, GREEN,
                "Production needs proof", text_size=15, radius=1.0)

    # Arrow between columns
    arrow_x = left_x + col_w + col_gap / 2
    for i in range(n):
        y = top_y - i * (row_h + gap) + row_h / 2
        arrow = FancyArrowPatch((left_x + col_w + 0.8, y),
                                (right_x - 0.8, y),
                                arrowstyle="-|>", mutation_scale=14,
                                color=GRAY, lw=1.5, alpha=0.5)
        ax.add_patch(arrow)

    for i, (proto, prod) in enumerate(rows):
        y = top_y - i * (row_h + gap)
        # Left column (prototype - light with gray border feel)
        rounded_box(ax, left_x, y, col_w, row_h, LIGHT, "", radius=0.8)
        ax.text(left_x + col_w / 2, y + row_h / 2, proto,
                ha="center", va="center", color=TEXT_DK,
                fontsize=12.5, fontfamily=BODY_FONT, style="italic")
        # Right column (production - light with teal accent)
        rounded_box(ax, right_x, y, col_w, row_h, "#E6F4F1", "", radius=0.8)
        ax.text(right_x + col_w / 2, y + row_h / 2, prod,
                ha="center", va="center", color=TEXT_DK,
                fontsize=12.5, fontfamily=BODY_FONT, fontweight="bold")

    # Bottom call-out
    rounded_box(ax, 4, 3, 92, 4.5, NAVY,
                "AgentOps bridges the gap with evaluation, gates, observability, and operational evidence.",
                text_size=12, bold=False, radius=1.0)

    save(fig, "production-gap.png")


# ---------------------------------------------------------------------------
# Diagram: model lifecycle upgrade process (canary flow)
# ---------------------------------------------------------------------------
def model_lifecycle():
    fig, ax = new_canvas()
    add_title(ax, "Model lifecycle and canary upgrades")
    add_subtitle(ax, "Treat every model change as a release candidate, not a config flip.")

    # Layout: horizontal flow of boxes with two parallel lanes (old model / new model)
    # Y positions
    lane_old_y = 36 if SHOW_HEADER else 32
    lane_new_y = lane_old_y - 20
    box_y = (lane_old_y + lane_new_y) / 2 - 2.5  # Centered between lanes
    box_h = 5
    lane_label_x = 2

    # Draw lane lines
    ax.plot([12, 96], [lane_old_y, lane_old_y], color=GRAY, lw=2.5, alpha=0.5)
    ax.plot([12, 96], [lane_new_y, lane_new_y], color=GREEN, lw=2.5, alpha=0.7)

    # Lane labels
    ax.text(lane_label_x, lane_old_y, "Old Model", ha="left", va="center",
            color=NAVY, fontsize=11, fontfamily=HEADING_FONT, fontweight="bold")
    ax.text(lane_label_x, lane_new_y, "New Model", ha="left", va="center",
            color=GREEN, fontsize=11, fontfamily=HEADING_FONT, fontweight="bold")

    # Process steps
    steps = [
        ("Current\nModel",        BLUE,   14),
        ("Deploy New\nAlongside",  TEAL,   28),
        ("Evaluate on\nSame Data", PURPLE, 42),
        ("Shadow\nTraffic",        ORANGE, 56),
        ("Canary\nRollout",        GREEN,  76),
        ("Retire\nOld",            "#C0392B", 90),
    ]
    box_w = 12
    for label, color, cx in steps:
        x = cx - box_w / 2
        rounded_box(ax, x, box_y, box_w, box_h, color, label,
                    text_size=11, radius=0.8)

    # Arrows between sequential boxes
    for i in range(len(steps) - 1):
        x1 = steps[i][2] + box_w / 2 + 0.3
        x2 = steps[i + 1][2] - box_w / 2 - 0.3
        # Skip arrow between Shadow Traffic and Canary (diamond goes there)
        if i == 3:
            continue
        arrow = FancyArrowPatch((x1, box_y + box_h / 2), (x2, box_y + box_h / 2),
                                arrowstyle="-|>", mutation_scale=14,
                                color=GRAY, lw=1.5)
        ax.add_patch(arrow)

    # Decision diamond: "Metrics OK?" between Shadow Traffic and Canary Rollout
    diamond_cx = 66
    diamond_cy = box_y + box_h / 2
    diamond_size = 3.5
    diamond = Polygon(
        [(diamond_cx, diamond_cy + diamond_size),
         (diamond_cx + diamond_size, diamond_cy),
         (diamond_cx, diamond_cy - diamond_size),
         (diamond_cx - diamond_size, diamond_cy)],
        closed=True, facecolor=GOLD, edgecolor=ORANGE, lw=1.5
    )
    ax.add_patch(diamond)
    ax.text(diamond_cx, diamond_cy, "Metrics\nOK?", ha="center", va="center",
            color=WHITE, fontsize=9, fontfamily=HEADING_FONT, fontweight="bold")

    # Arrow: Shadow Traffic -> diamond
    arrow = FancyArrowPatch(
        (steps[3][2] + box_w / 2 + 0.3, box_y + box_h / 2),
        (diamond_cx - diamond_size - 0.3, diamond_cy),
        arrowstyle="-|>", mutation_scale=14, color=GRAY, lw=1.5)
    ax.add_patch(arrow)

    # Arrow: diamond -> Canary Rollout (yes path)
    arrow = FancyArrowPatch(
        (diamond_cx + diamond_size + 0.3, diamond_cy),
        (steps[4][2] - box_w / 2 - 0.3, box_y + box_h / 2),
        arrowstyle="-|>", mutation_scale=14, color=GRAY, lw=1.5)
    ax.add_patch(arrow)

    # "No - iterate" arrow: curves UP and OVER from diamond back to "Evaluate on Same Data"
    # Arc goes above the boxes (connectionstyle rad positive = curve upward)
    eval_box_cx = steps[2][2]
    no_arrow = FancyArrowPatch(
        (diamond_cx, diamond_cy + diamond_size + 0.2),
        (eval_box_cx, box_y + box_h + 0.3),
        connectionstyle="arc3,rad=0.4",
        arrowstyle="-|>", mutation_scale=14,
        color="#C0392B", lw=1.8, alpha=0.85)
    ax.add_patch(no_arrow)
    # Label for the No arrow
    ax.text((diamond_cx + eval_box_cx) / 2, box_y + box_h + 4.5,
            "No \u2013 iterate", ha="center", va="center",
            color="#C0392B", fontsize=10, fontfamily=BODY_FONT, fontweight="bold")

    # Old model X at the end
    ax.text(96.5, lane_old_y, "\u2716", ha="center", va="center",
            color="#C0392B", fontsize=18)

    # Progressive rollout percentages below new model lane
    percentages = ["5%", "10%", "25%", "50%", "100%"]
    pct_x_start = 68
    pct_spacing = 5.5
    for i, pct in enumerate(percentages):
        ax.text(pct_x_start + i * pct_spacing, lane_new_y - 2.5, pct,
                ha="center", va="center", color=GREEN, fontsize=9,
                fontfamily=BODY_FONT)
    ax.text(pct_x_start + 2 * pct_spacing, lane_new_y - 4.5, "Progressive rollout",
            ha="center", va="center", color=GRAY, fontsize=9,
            fontfamily=BODY_FONT, style="italic")

    save(fig, "model-lifecycle-upgrade-process.png")


# ---------------------------------------------------------------------------
# Registry
# ---------------------------------------------------------------------------
DIAGRAMS = {
    "complexity-ladder": complexity_ladder,
    "operating-loop": operating_loop,
    "agentops-four-pillars": four_pillars,
    "maturity-ribbon": maturity_ribbon,
    "foundry-control-plane": foundry_control_plane,
    "telemetry-to-action": telemetry_to_action,
    "red-teaming-taxonomy": red_teaming_taxonomy,
    "day2-quadrant": day2_quadrant,
    "anatomy-complexity": anatomy_complexity,
    "production-gap": production_gap,
    "model-lifecycle": model_lifecycle,
}


def main():
    global SHOW_HEADER
    args = sys.argv[1:]
    if "--no-header" in args:
        SHOW_HEADER = False
        args.remove("--no-header")
    targets = args or ["all"]
    if "all" in targets:
        targets = list(DIAGRAMS.keys())
    for t in targets:
        if t not in DIAGRAMS:
            print(f"unknown diagram: {t}")
            continue
        print(f"rendering: {t}")
        DIAGRAMS[t]()
    print("done.")


if __name__ == "__main__":
    main()
