docker build  --no-cache ^
 --build-arg GID=\" $(id -g $USER) \" --build-arg UID=\" $(id -u $USER) \" ^
 -f "/home/anandhu/CM/repos/anandhu-eng@cm4mlops/script/app-mlperf-inference/dockerfiles/ubuntu_22.04.Dockerfile" ^
 -t "local/cm-script-app-mlperf-inference-generic--reference--mixtral-8x7b--pytorch--cpu--test--r4.1-dev-default--offline:ubuntu-22.04-latest" ^
 .
