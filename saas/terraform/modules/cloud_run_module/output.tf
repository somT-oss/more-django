output "cloudrun_url" {
    value = google_cloud_run_v2_service.communely_cloud_run_instance.uri
}