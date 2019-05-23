#!/bin/sh

nvidia-smi --query-gpu=gpu_name,temperature.gpu,memory.used,memory.total,driver_version --format=csv,noheader | awk -F "," '{print $1 " " $2"°C " $3 " /" $4 " " $5}'
