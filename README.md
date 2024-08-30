# AWS Python Boto3 Scripts

This repository contains various Python scripts that interact with AWS services using the Boto3 library. These scripts are part of my AWS Academy Cloud Developing course and personal learning exercises.

## Scripts

### 1. `describe_instances.py`

This script describes the EC2 instances associated with your AWS account. It uses the Boto3 client API to retrieve detailed information about each instance, such as its ID, state, type, and other metadata.

### 2. `listS3.py`

This script lists all the S3 buckets in your AWS account. It utilizes the Boto3 client API to interact with the S3 service and fetch the list of buckets.

### 3. `listS3_using_resource.py`

This script lists all the S3 buckets using the Boto3 resource API instead of the client API. The resource API provides a higher-level, more Pythonic way of interacting with AWS services.

### 4. `s3-permission.py`

This script manages S3 bucket permissions and public access settings. It performs the following actions:
- **Bucket Ownership Control**: Sets the S3 bucket ownership control to `BucketOwnerPreferred`, ensuring that the bucket owner has full control over objects in the bucket.
- **Public Access Block**: Disables the public access block settings, allowing for public access to the bucket.
- **Public Object Access**: Grants public read access to a specific file (`index.html`) within the S3 bucket.

### Client API vs. Resource API

- **Client API**: The client API provides low-level access to AWS services. It directly maps to the AWS service API operations. This API is more detailed and requires you to manage pagination and other service-specific operations.

- **Resource API**: The resource API provides a higher-level, more Pythonic interface. It abstracts away some of the complexities of the client API, offering a more intuitive way to interact with AWS services. It's particularly useful for operations that involve working with multiple related AWS resources.

## Prerequisites

- Python 3.9 or later
- Boto3 library installed
- AWS credentials configured (either via environment variables, AWS CLI, or IAM roles)

## How to Run

1. Clone this repository:
    ```bash
    git clone https://github.com/VDKamani/aws-python-boto3.git
    cd aws-python-boto3
    ```

2. Install dependencies:
    ```bash
    pip install boto3
    ```

3. Run the desired script:
    ```bash
    python describe_instances.py
    ```

## Acknowledgments

- AWS Academy Cloud Developing Course
- [Boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
