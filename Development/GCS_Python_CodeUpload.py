from gcloud import storage
storageClient = storage.client()
bucket = storageClient.get_bucket("myApplicationBucket")
blob = bucket.blob("app/new_file.txt")
blob.upload_from_filename("./MyApplication.txt")