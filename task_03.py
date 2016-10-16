#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A complex testcase task_03."""

EXPENSE = 14.23
LOOKS_NICE = True
MAX_EXPENSE = 12
GET_OUT_ALIVE = False

SACRIFICE = ((LOOKS_NICE and EXPENSE <= MAX_EXPENSE) or
             (not GET_OUT_ALIVE and not(LOOKS_NICE and EXPENSE <= MAX_EXPENSE)))
