# Medical-Image-DL-Pipeline-MLOps
This repo hosts an MLOps project, demonstrating a CI/CD pipeline for medical image analysis. It focuses on classifying medical images using CNN. The project utilizes tools like DVC, MLflow &amp; Jenkins to automate and streamline the training, evaluation, and deployment of the model. A Flask-based API is implemented to serve the model for prediction.


## Workflows

1. Update config.yaml
2. Update params.yaml
3. Update the entity
4. Update the configuration manager in src config
5. Update the components
6. Update the pipeline
7. Update the main.py
8. Update the dvc.yaml




























## Command Prompt Shortcuts:

- To create directory/Folder = `mkdir <name>`
- To remove directory/Folder = `rmdir <name>`
- To create file = `type nul > app.py (type nul > template.py)`
- to create file using CMD/Powershell : `type <filename> (type template.py)`

## Vertual environment related shortcuts

- To create environment = `conda create -p flask_env -y`
- To check available envs = `conda env list`
- To check available envs = `conda info --envs`
- To activate environment = `conda activate flask_env`
- To install requirements.txt = `pip install -r requirements.txt`

##  Package related 

- To check install packages = `pip list`
- To check detailed about package = `pip show package_name`
- To install package = `pip install package_name`
- To uninstall package = `pip uninstall package_name`
- To check python installed version = `python --version`

## Git Command

- To add all file = `git add .`

- To add any particular file = `git add <file_name>`

- To commit = `git commit -m "commit message"`

- To push the code = `git push origin main`






## Problem/Issue:

### ⚠️ Common Installation Issue (Windows + Python < 3.9)

If you're installing from `requirements.txt` and encounter the following error:

```
Collecting pywinpty>=2.0.1 (from jupyter-server<3,>=2.4.0->notebook->-r requirements.txt (line 6))
  Using cached pywinpty-2.0.14.tar.gz (27 kB)
  Installing build dependencies ... done
  Getting requirements to build wheel ... done
  Installing backend dependencies ... error
  error: subprocess-exited-with-error

  × pip subprocess to install backend dependencies did not run successfully.
  │ exit code: 1
  ╰─> [3 lines of output]
      ERROR: Ignored the following versions that require a different python version: 
        0.1.0 Requires-Python >=3.9; 
        0.1.1 Requires-Python >=3.9; 
        0.1.2 Requires-Python >=3.9; 
        0.1.3 Requires-Python >=3.9; 
        0.1.4 Requires-Python >=3.9; 
        0.1.5 Requires-Python >=3.9
      ERROR: Could not find a version that satisfies the requirement puccinialin (from versions: none)
      ERROR: No matching distribution found for puccinialin
```

## ✅ Solution That Worked for Me:

This issue is often caused by:

- Outdated `pip`, `setuptools`, or `wheel`

- Using an older Python version (below 3.9)

To fix it, simply run the following before installing requirements:

```CMD
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

> This resolved the error in my case.<br>
> If you're still facing issues, make sure your Python version is 3.9 or higher.

- [Data Link](https://drive.usercontent.google.com/download?id=1z0mreUtRmR-P-magILsDR3T7M6IkGXtY&export=download&authuser=0)

- [Data Link](https://universe.roboflow.com/student-jovgq/ct-scan-dgzcv)