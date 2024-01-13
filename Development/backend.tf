terraform {
    required_version = "~>1.5"
    backend "gcs" {
      bucket = "MyIAC_State"
      prefix = "terraform/IaC"
    }
}

provider "google" {
  project = "project123"
}