variable "project_id" {
  description = "GCP project ID"
  type        = string
}

variable "region" {
  description = "GCP region"
  type        = string
  default     = "europe-west2"
}

variable "location" {
  description = "GCP resource location (EU or US)"
  type        = string
  default     = "EU"
}

variable "credentials_file" {
  description = "Path to GCP service account key JSON"
  type        = string
}

variable "bucket_name" {
  description = "Globally unique GCS bucket name"
  type        = string
}

variable "bq_dataset_id" {
  description = "BigQuery dataset ID"
  type        = string
}

variable "bq_friendly_name" {
  description = "BigQuery dataset friendly name"
  type        = string
  default     = "Demo dataset"
}

variable "bq_description" {
  description = "BigQuery dataset description"
  type        = string
  default     = "Dataset created by Terraform"
}
