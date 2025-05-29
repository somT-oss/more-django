variable "project_id" {
    description = "project_id"
    type = string
}
variable "name" {
    description = "cloudrun instance name"
    type = string
    default = "communely-cloudrun-instance"
}

variable "location" {
    description = "location of cloudrun instance"
    type = string
    default = "us-central1"
}

variable "docker_image" {
  description = "docker image url"
  type = string
}

variable "GS_BUCKET_NAME" {
  description = "communely bucket name"
  type = string
}

variable "env_vars" {
  type = map(string)
  default = {
    ENV = "prod"
  }
}