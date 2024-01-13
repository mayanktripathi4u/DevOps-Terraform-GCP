# DevOps-Terraform-GCP
Devops : CI/CD Pipeline for GCP using Terraform and Github Actions 


In this we are trying to create a simple CI/CD Pipeline which will
    * Create / Provision and manage the Infrastrcuture on Google Cloud
    * Push the Code changes into Google Storage bucket.


# Setup
1. Create a Git Repo, and clone it to your local.
2. Create below folder structure
    .github/workflows
    Development
        <all terraform and application related files.>
3. Under `Development` folder we will have all our Terraform files such as "main.tf", "backend.tf" and the application related files such as "MyApplication.txt" & also some additonal files which we will be using to upload the code from local to Google Storage using Python Code "GCS_Python_CodeUpload.py".
4. In "workflows" create the yaml file as "cicd_pipeline.yml".
5. Create a `Service Account` in Google Cloud, and store the credentials in the GitHub `Secrets and Variables` to use in workflow yaml file.



# How to Run
1. Create a Branch (Optional) or work directly on Main.
2. Make some changes into the files under folder "Development".
    May be modify the existing file "MyApplication.txt" 
    Or
    Upload new files.
3. Commit the changes into Branch (if using branch)
        <git status>
        <git add .>
        <git commit -m "change description">
        <git push -u origin branch_name>

    or
    If branch is not used..
        <git push origin master>

4. This should trigger the GitHub Actions.. which we could go into GitHub browser --> Actions tab and check.
    However as we have a condition to have a check if "main" branch has changes then only perform "terraform apply" and "python upload", apart from this rest all git workflow will run.

5. Next if used branch then go with the `Pull Request (PR)` and merge the changes. Once merged GitHub Actions will get trigger again, and now as this is in `main`, "terraform apply" and "python upload" will also run.




