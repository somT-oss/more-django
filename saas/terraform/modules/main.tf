module "bucket_module" {
    source = "./bucket_module"
    project_id = var.project_id
    bucket_name = var.bucket_name
    service_account = module.service_account.email
}

module "service_account" {
    source = "./service_account_module"
    project_id = var.project_id
    service_account_id = var.service_account_id
    service_account_name = var.service_account_name
}

module "cloud_run" {
  source = "./cloud_run_module"
  project_id = var.project_id
  docker_image = var.docker_image
}