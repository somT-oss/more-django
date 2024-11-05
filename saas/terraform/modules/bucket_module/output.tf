output "communely_media_bucket_name" {
	description = "communely profile picture bucket value"
	value = google_storage_bucket.communely_media_bucket
}


output "communely_media_bucket_location" {
	description = "communely profile picture bucket location"
	value = google_storage_bucket.communely_media_bucket.location
}
