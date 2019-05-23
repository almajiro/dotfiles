#!/usr/bin/env bash
lscpu | awk '/CPU MHz/ {printf("%.1f GHz",$3/1000); }'
