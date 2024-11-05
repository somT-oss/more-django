resource "google_service_account" "communely_service_account" {
    project = var.project_id
    account_id = var.service_account_id
    display_name = var.service_account_name
}
