variable "gcp_project_id" {
  type        = string
  description = "Google Cloud project ID"
  default     = "{{ cookiecutter.gcp_project_id }}"
}

variable "gcp_region" {
  type        = string
  description = "GCP region for deployment"
  default     = "{{ cookiecutter.gcp_region }}"
}

variable "function_name" {
  type        = string
  description = "Name of the Cloud Function"
  default     = "{{ cookiecutter.function_name }}"
}

variable "runtime" {
  type        = string
  description = "Runtime for the Cloud Function"
  default     = "python{{ cookiecutter.python_version.replace('.', '') }}"
}

variable "entry_point" {
  type        = string
  description = "Entry point function for the Cloud Function"
  default     = "main"
}

variable "memory" {
  type        = number
  description = "Memory allocated to the Cloud Function (in MB)"
  default     = 256
}

variable "timeout" {
  type        = string
  description = "Timeout for the Cloud Function (in seconds)"
  default     = "60s"
}

variable "source_dir" {
  type        = string
  description = "Directory containing the function code"
  default     = "../function"
}
