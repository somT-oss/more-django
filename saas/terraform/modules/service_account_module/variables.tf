variable "service_account_id" {
    type = string
    description = "Service Account id"
}

variable "service_account_name" {
    type = string
    description = "Service Account name"
}

variable "project_id" {
  type = string
  description = "Project id"
}

output "email" {
  value = google_service_account.communely_service_account.email
}