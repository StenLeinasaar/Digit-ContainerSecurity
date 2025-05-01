provider "aws" {
  region = "us-east-1"
}

# Publicly readable S3 bucket with no encryption
resource "aws_s3_bucket" "public_bucket" {
  bucket = "trivy-demo-public-bucket"
  acl    = "public-read"

  server_side_encryption_configuration {
    # missing encryption block → HIGH severity
  }
}
