from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, installed_version):
    if not installed_version:
        return

    # Link existing config params to XML ids.
    config_params = ["default_invoice_email_template", "default_confirmation_template"]
    module = "sale"
    for name in config_params:
        record = env["ir.config_parameter"].search([("key", "=", f"{module}.{name}")])
        if not record:
            continue
        openupgrade.add_xmlid(env.cr, module, name, "ir.config_parameter", record.id)
