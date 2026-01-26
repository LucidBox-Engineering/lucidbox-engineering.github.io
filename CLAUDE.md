# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a static website for LucidBox Engineering & Consulting Ltd., built using Pelican (Python-based static site generator). The site is deployed to GitHub Pages via GitHub Actions.

## Build and Development Commands

This project uses [just](https://github.com/casey/just) as a command runner to standardize tasks.

### Common commands
```bash
just build    # Development build (uses pelicanconf.py)
just dev      # Build and serve with auto-reload
```

### Production build
```bash
# Production build (uses publishconf.py with SITEURL set)
uv run pelican content -o deploy -s publishconf.py
```

### Local development
Run `just dev` to start the development server with auto-reload. The site will be available at http://localhost:8000.

### Testing changes
After making changes, run `just build` and open `output/index.html` in a browser, or use `just dev` for live preview.

## Architecture

### Project Structure
- **content/pages/**: Markdown files for site pages (About, Services, Contact, etc.)
  - Each page has metadata (Title, Order, Template, Theme) in the frontmatter
  - Pages are ordered by the `Order` field (pelicanconf.py:35)

- **theme/**: Custom Pelican theme
  - **templates/**: Jinja2 templates for rendering pages
    - `base.html`: Root template with HTML structure, CSS loading, and analytics
    - `nav_base.html`: Base template with navigation header and footer (includes contact form)
    - `index.html`: Landing page template
    - `page.html`: Generic page wrapper
    - Template-specific files: `about.html`, `services.html`, `engagement.html`, `404.html`
  - **static/css/**: Custom CSS (lucidbox.css)
  - **static/fonts/**: Custom fonts (PPFraktionMono)
  - **templates/svg/**: SVG icons and graphics used throughout the site

- **pelicanconf.py**: Development configuration
  - Sets THEME, SITENAME, contact info (email, phone, address)
  - Configures page ordering, URL structure, and static paths
  - Disables feeds, categories, and tags

- **publishconf.py**: Production configuration
  - Imports pelicanconf.py and overrides SITEURL to https://lucidbox.ca
  - Used by CI/CD for deployment builds

### Template System
The site uses a three-tier template inheritance:
1. `base.html` - Provides HTML structure, meta tags, CSS loading, analytics script
2. `nav_base.html` - Extends base, adds navigation header and footer with contact form
3. Page-specific templates extend nav_base and fill in the `section` block

Pages can specify a custom `Template` in their frontmatter (e.g., Template: about) to use a specific template instead of the generic page.html.

### Navigation
Navigation is generated from the pages defined in content/pages/. The ORDER of pages is controlled by the `Order` metadata field in each page's frontmatter. Lower numbers appear first.

### Contact Form
The contact form (in nav_base.html:39-60) submits to an AWS Lambda endpoint. The form handler is inline JavaScript that shows success/error messages.

### Theme Variants
Pages can specify `Theme: light` in their frontmatter to use a light background variant (affects logo and navigation styling).

## Deployment

The site deploys automatically on every push to main via GitHub Actions (.github/workflows/build-site.yml):
1. Installs uv and Python 3.12
2. Runs production build: `uv run pelican content -o deploy -s publishconf.py`
3. Force-pushes the deploy directory to the gh-pages branch

The gh-pages branch is served by GitHub Pages at https://lucidbox.ca

## Configuration Details

- Python version is locked to 3.12 (pyproject.toml:6)
- Uses uv for dependency management
- Uses just for task running (see justfile for available commands)
- Analytics: GoatCounter at analytics.lucidbox.ca (base.html:30)
- Contact info variables are defined in pelicanconf.py (lines 47-50) and used throughout templates
