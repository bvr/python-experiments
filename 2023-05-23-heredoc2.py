
def files2():
    return [
        'afq80.txt',
        'arts80.txt',
        'af_cq40.txt',
        'af_cp40.txt',
        'mnt_cq05.txt',
    ]

def files():
    return """
afq80.txt
arts80.txt
af_cq40.txt
af_cp40.txt
mnt_cq05.txt
""".strip().split('\n')

files = dict([(f,1) for f in files()])
print(files)
