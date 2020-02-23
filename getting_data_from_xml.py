#!/usr/bin/env python3
# -*- coding: utf8 -*-
import os
from xml.etree import ElementTree


tree = ElementTree.parse(os.path.join('xml','data.xml'))
root = tree.getroot()
