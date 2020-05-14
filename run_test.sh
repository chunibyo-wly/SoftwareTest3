#!/usr/bin/env bash
report="/var/www/nginx/report"

if [ ! -d $report ]; then
  mkdir -p $report
fi

pytest test/*.py --html=$report/index.html
