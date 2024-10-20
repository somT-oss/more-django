resource "google_storage_bucket" "communely_media_bucket" {
	project = var.project_id
	name = var.bucket_name
	force_destroy = var.force_destroy_option
	
  	public_access_prevention = var.bucket_visibility
  	location = var.bucket_location
	
} 

resource "google_storage_bucket_iam_member" "object_viewer_creator" {
  bucket = google_storage_bucket.communely_media_bucket.name
  role = "roles/storage.objectCreator"
  member = var.service_account
}