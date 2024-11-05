output "service_account_id" {
    description = "Service Account Id"
    value = google_service_account.communely_service_account.id
}

output "service_account_email" {
    description = "Service Account Email Address"
    value = google_service_account.communely_service_account.email
}

output "service_account_name" {
    description = "Service account name"
    value = google_service_account.communely_service_account.name
}