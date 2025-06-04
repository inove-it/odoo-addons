from urllib.parse import urlparse

from odoo import api, fields, models


class Website(models.Model):
    _inherit = "website"

    has_umami_analytics = fields.Boolean("Umami Analytics")
    umami_analytics_id = fields.Char(
        "Umami website ID",
        help="The ID Umami uses to identify the website",
        default="1",
    )
    umami_analytics_host = fields.Char(
        "Umami host",
        help="The host/path your umami script installation is "
        "accessible by on the internet.",
    )
