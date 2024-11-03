provider "google" {
  project = var.gcp_project_id
  region  = var.gcp_region
}

# Archive the function code
data "archive_file" "function_zip" {
  type        = "zip"
  source_dir  = var.source_dir
  output_path = "${path.module}/function.zip"
}

# Create a GCS bucket for storing the function code
resource "google_storage_bucket" "function_bucket" {
  name                        = "${var.gcp_project_id}-function-source"
  location                    = var.gcp_region
  uniform_bucket_level_access = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "Delete"
    }
  }
}

# Upload the function code to the GCS bucket
resource "google_storage_bucket_object" "function_archive" {
  name   = "${var.function_name}.zip"
  bucket = google_storage_bucket.function_bucket.name
  source = data.archive_file.function_zip.output_path
}

# Deploy the Cloud Function
resource "google_cloudfunctions_function" "function" {
  name        = var.function_name
  description = "Cloud Function deployed via Terraform"

  runtime       = var.runtime
  entry_point   = var.entry_point
  region        = var.gcp_region

  source_archive_bucket = google_storage_bucket.function_bucket.name
  source_archive_object = google_storage_bucket_object.function_archive.name

  trigger_http = true

  available_memory_mb   = var.memory
  timeout               = var.timeout
  ingress_settings      = "ALLOW_ALL"

  # Optional: Set environment variables
  # environment_variables = {
  #   KEY = "value"
  # }
}

# Allow unauthenticated invocations
resource "google_cloudfunctions_function_iam_member" "invoker" {
  project        = var.gcp_project_id
  region         = var.gcp_region
  cloud_function = google_cloudfunctions_function.function.name

  role   = "roles/cloudfunctions.invoker"
  member = "allUsers"
}
