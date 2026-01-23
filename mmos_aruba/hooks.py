app_name = "mmos_aruba"
app_title = "MMOS Aruba"
app_publisher = "MMOS"
app_description = "Gestisce account e nodi Aruba Cloud per Press"
app_email = "dev@onekeyco.com"
app_license = "MIT"

app_version = "0.1.0"

after_install = "mmos_aruba.install.after_install"

whitelisted_methods = [
    "mmos_aruba.api.sync.get_nodes_summary",
    "mmos_aruba.api.sync.update_node_status",
]
