variable "project_id" {
	description = "Project ID"
	type = string
}

variable "bucket_name" {
	description = "Profile picture bucket name"
	type = string
}

variable "bucket_visibility" {
	description = "Visibility settings of the bucket"
	type = string
	default = "enforced"
}

variable "force_destroy_option" {
	description = "Destroy bucket data and metadata upon deletion"
	type = bool
	default = true
}

variable "bucket_location" {
	description = "Bucket location"
	type = string
	default = "US"
}

variable "service_account" {
	description = "Service account connected to gcp bucket"
	type = string
}