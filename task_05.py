#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Docstring for task_05."""


BP_ANSWER = int(raw_input('What is your blood pressure? '))

if BP_ANSWER <= 89:
    BP_STATUS = 'Low!'
elif BP_ANSWER <= 119:
    BP_STATUS = 'Ideal!'
elif BP_ANSWER <= 139:
    BP_STATUS = 'Warning!'
elif BP_ANSWER <= 159:
    BP_STATUS = 'High!'
else:
    BP_STATUS = 'Emergency!'

OUTPUT = 'Your status is currently: {}'.format(BP_STATUS)
print OUTPUT
