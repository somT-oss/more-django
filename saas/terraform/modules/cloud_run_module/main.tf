resource "google_cloud_run_v2_service" "communely_cloud_run_instance" {
    project = var.project_id
    name = var.name
    location = var.location
    deletion_protection = false
  template {  
    containers {
        image = var.docker_image
        dynamic "env" {
          for_each = var.env_vars
          content {
            name = env.key
            value = env.value
          }  
        }
    }
  }
}