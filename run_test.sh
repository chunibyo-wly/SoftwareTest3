#!/usr/bin/env bash
mkdir report
pytest test/*.py --html=./report/index.html
