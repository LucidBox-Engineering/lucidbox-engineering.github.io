from datetime import datetime

AUTHOR = "LucidBox"
SITENAME = "LucidBox Engineering &amp; Consulting Ltd."
SITEURL = ""
THEME = "theme"

PATH = "content"

TIMEZONE = "America/Edmonton"

DEFAULT_LANG = "en"
DEFAULT_DATE_FORMAT = "%Y-%m-%d"

STATIC_PATHS = ["images", "extra/CNAME", "images/favicon/favicon.ico"]
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
    "images/favicon/favicon.ico": {"path": "favicon.ico"},
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# We don't bother generating categories
CATEGORY_SAVE_AS = ""
CATEGORIES_SAVE_AS = ""
# or tags
TAGS_SAVE_AS = ""
TAG_SAVE_AS = ""

PAGE_ORDER_BY = "order"

DEFAULT_PAGINATION = False

# Disabled for now so that we can launch with just a simple landing page
DISPLAY_PAGES_ON_MENU = True

# For use in the copyright footer
YEAR = datetime.now().year

CONTACT_EMAIL = "contact@lucidbox.ca"
CONTACT_PHONE = "+1 (587) 316 8828"
CONTACT_PHONE_CLEAN = "+15873168828"
CONTACT_ADDRESS = "5005 Dalhousie Dr NW 175 #1527 Calgary, AB T3A 5R8"

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
