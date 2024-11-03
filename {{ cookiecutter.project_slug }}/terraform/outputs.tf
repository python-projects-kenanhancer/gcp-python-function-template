output "function_name" {
  description = "The name of the deployed Cloud Function"
  value       = google_cloudfunctions_function.function.name
}

output "function_region" {
  description = "The region where the Cloud Function is deployed"
  value       = google_cloudfunctions_function.function.region
}

output "function_url" {
  description = "The URL of the deployed Cloud Function"
  value       = google_cloudfunctions_function.function.https_trigger_url
}
