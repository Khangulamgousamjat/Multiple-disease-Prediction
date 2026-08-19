"""
theme.py — Centralized design token system.
Single source of truth for all colors, typography, spacing and radius values.
"""

# ── Backgrounds ──────────────────────────────────────────────────────────────
BG_PRIMARY   = "#0A0A0A"
BG_SECONDARY = "#111111"
BG_CARD      = "#161616"
BG_CARD_ALT  = "#1A1A1A"
BG_SIDEBAR   = "#0D0D0D"

# ── Wine-Red Accent Palette ───────────────────────────────────────────────────
WINE_RED        = "#8B1E2D"
WINE_RED_HOVER  = "#A52A3A"
WINE_RED_ACTIVE = "#6E1423"
WINE_RED_DEEP   = "#5A0F1B"
WINE_RED_LIGHT  = "#C0394A"
WINE_RED_MUTED  = "rgba(139, 30, 45, 0.15)"
WINE_RED_BORDER = "rgba(139, 30, 45, 0.3)"

# ── Text ──────────────────────────────────────────────────────────────────────
TEXT_PRIMARY   = "#F2F2F2"
TEXT_SECONDARY = "#9A9A9A"
TEXT_MUTED     = "#5A5A5A"
TEXT_DARK      = "#2E2E2E"
TEXT_ACCENT    = "#C0394A"

# ── Borders ───────────────────────────────────────────────────────────────────
BORDER       = "#1C1C1C"
BORDER_ALT   = "#222222"
BORDER_HOVER = "#333333"
BORDER_FOCUS = WINE_RED

# ── Semantic Colors ───────────────────────────────────────────────────────────
SUCCESS      = "#2D6A4F"
SUCCESS_BG   = "#0D2018"
SUCCESS_TEXT = "#6FCF97"

WARNING      = "#A67C00"
WARNING_BG   = "#1A1500"
WARNING_TEXT = "#F2C94C"

ERROR        = WINE_RED
ERROR_BG     = "#1A0508"
ERROR_TEXT   = "#E57373"

# ── Typography ────────────────────────────────────────────────────────────────
FONT_FAMILY  = "'Inter', 'Segoe UI', -apple-system, BlinkMacSystemFont, sans-serif"
GOOGLE_FONTS = "https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap"

FONT_XS   = "11px"
FONT_SM   = "13px"
FONT_MD   = "15px"
FONT_LG   = "18px"
FONT_XL   = "24px"
FONT_2XL  = "32px"
FONT_3XL  = "42px"
FONT_HERO = "56px"

# ── Spacing ───────────────────────────────────────────────────────────────────
SPACE_XS  = "4px"
SPACE_SM  = "8px"
SPACE_MD  = "16px"
SPACE_LG  = "24px"
SPACE_XL  = "40px"
SPACE_2XL = "64px"

# ── Border Radius ─────────────────────────────────────────────────────────────
RADIUS_SM   = "4px"
RADIUS_MD   = "8px"
RADIUS_LG   = "12px"
RADIUS_XL   = "16px"
RADIUS_FULL = "9999px"

# ── Shadows ───────────────────────────────────────────────────────────────────
SHADOW_SM   = "0 1px 3px rgba(0,0,0,0.5)"
SHADOW_MD   = "0 4px 12px rgba(0,0,0,0.6)"
SHADOW_LG   = "0 8px 28px rgba(0,0,0,0.7)"
SHADOW_WINE = "0 4px 20px rgba(139,30,45,0.25)"
