import os


def rid(i,base64):
    os.makedirs('pic',exist_ok=True)
    with open(os.path.join('pic',i+'.txt'),'w') as f:
        f.write(base64)
