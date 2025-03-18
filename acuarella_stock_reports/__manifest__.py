{
    "name": "Acuarella Stock Reports",
    "author": "Odoo PS",
    "maintainer": "Odoo PS",
    "website": "https://www.odoo.com",
    "category": "Custom Development",
    "version": "18.0.1.0.0",
    "depends": ["sale_stock", "stock_picking_batch", "stock_delivery"],
    "data": [
        "reports/external_layouts.xml",
        "reports/report_picking_batch_acuarella.xml",
        "data/stock_picking_batch_reports.xml",
        "views/sale_order_views.xml",
        "views/stock_picking_batch_views.xml",
        "views/stock_picking_views.xml",
    ],
    "demo": [
        "data/acuarella_stock_reports_demo.xml",
    ],
    "assets": {
        "web.report_assets_common": [
            "acuarella_stock_reports/static/src/scss/acuarella_reports.scss",
        ],
    },
    "license": "OEEL-1",
}
