
"""Import External Libraries"""
from hashlib import sha256, md5


"""Variables"""
DoB: str = ""  # Date of Birth
No: str = ""  # Phone Number
    
# in order to guarantee the safety of data encryption, the algorithm of Salt won't be disclosed.
Salt: str = ""


""" Main Program """
UID_raw = DoB + No + Salt  # Notice: this is only a demonstration, not necessarily means the combaniant order of data.
UID_SHA256 = sha256(UID_raw.encode('uft-8')).hexdigest()
UID = md5(UID_SHA256.encode('uft-8')).digest()

# And hereinabove, a unique UID for each questionnaire has been created.
