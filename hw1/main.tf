terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "7.16.0"
    }
  }
}

provider "google" {
  credentials = file(var.credentials_file)
  project     = var.project_id
  region      = var.region
}

resource "google_storage_bucket" "demo_bucket" {
  name          = var.bucket_name
  location      = var.location
  force_destroy = true

  lifecycle_rule {
    condition { age = 3 }
    action    { type = "Delete" }
  }

  lifecycle_rule {
    condition { age = 1 }
    action    { type = "AbortIncompleteMultipartUpload" }
  }
}

resource "google_bigquery_dataset" "demo_dataset" {
  dataset_id                 = var.bq_dataset_id
  location                   = var.location
  delete_contents_on_destroy = true

  friendly_name = var.bq_friendly_name
  description   = var.bq_description
}
