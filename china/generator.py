# -*- coding:utf-8 -*-
__author__ = 'NaVient'

import json
import random

if  __name__ == '__main__':
    with open('firstname.json') as f:
        firstname = json.loads(f.read())

    with open('lastname.json') as f:
        lastname = json.loads(f.read())


    for i in range(10):
        name = [lastname[random.randrange(len(lastname) - 1)] + \
                firstname[random.randrange(len(firstname) - 1)] + \
                firstname[random.randrange(len(firstname) - 1)],
                lastname[random.randrange(len(lastname) - 1)] + \
                firstname[random.randrange(len(firstname) - 1)]
                ]
        print random.choice(name)
