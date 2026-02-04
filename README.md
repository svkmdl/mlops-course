# mlops-course
Practicing mlops

## Clone repo

```commandline
git clone https://github.com/svkmdl/mlops-course.git
```

## Setup virtual env and install requirements

```commandline
virtualenv .mlops_course_env
source .mlops_course_env/bin/activate
pip3 install requirements.txt
```

## Install vercel-cli (macos)
```commandline
brew install vercel-cli
```

## Check vercel installation
```commandline
vercel --version
```

## Log into vercel
```commandline
vercel login
```

## Deploy
```commandline
vercel .
```