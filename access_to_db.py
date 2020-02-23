#!/usr/bin/env python3
# -*- coding: utf8 -*-
import sqlalchemy as sa


engine = sa.create_engine(r"postgresql://blinov:GE1vmEN@217.71.129.139:4194/ias", echo=False)