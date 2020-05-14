#!/usr/bin/env bash
mkdir report
pytest test/*.py --html=/var/www/nginx/report/index.html
