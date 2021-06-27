import re

def del_upper(new_id):
    return new_id.lower()

def del_otherCharacter(new_id):
    pattern=re.compile('[\w\-\_\.]')
    match=pattern.findall(new_id)
    return ''.join(match)

def del_dot(new_id):
    return '.'.join(new_id.replace('.',' ').strip().split())

def empty_short(new_id):
    if len(new_id)==0:
        new_id='a'
    return new_id

def del_to16(new_id):
    return del_dot(new_id[:15])

def recommand(new_id):
    if len(new_id)<=2:
        while len(new_id)<3:
            new_id+=new_id[-1]
    return new_id

def solution(new_id):
    new_id = del_upper(new_id)
    new_id=del_otherCharacter(new_id)
    new_id= del_dot(new_id)
    new_id=empty_short(new_id)
    new_id=del_to16(new_id)
    new_id=recommand(new_id)
    return new_id