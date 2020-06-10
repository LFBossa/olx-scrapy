#!/usr/bin/bash
rm database.json
python downloader.py
python converter.py