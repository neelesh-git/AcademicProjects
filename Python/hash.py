#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 18:03:21 2019

@author: neeleshbhajantri
"""
import json
import emoji
with open(r"anderson.json","r",encoding="utf-8") as fh:
    for line in fh:
      data = json.load(fh)

def extract_emojis(str):
  return ''.join(c for c in str if c in emoji.UNICODE_EMOJI)