from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    has_umami_analytics = fields.Boolean(
        "Umami Analytics",
        related="website_id.has_umami_analytics",
        readonly=False,
    )
    umami_analytics_id = fields.Char(
        related="website_id.umami_analytics_id", readonly=False
    )
    umami_analytics_host = fields.Char(
        related="website_id.umami_analytics_host", readonly=False
    )
