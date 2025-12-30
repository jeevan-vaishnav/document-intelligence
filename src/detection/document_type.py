# pan
# aadhaar
# unknown

import re

def detect_document_type(text:str) -> str:
    """
    Detect document type: PAN / AADHAAR / UNKNOWN
    """

    pan_pattern = r"[A-Z]{5}[0-9]{4}[A-Z]"
    aadhaar_pattern = r"\d{4}\s?\d{4}\s?\d{4}"
    pan_match = re.search(pan_pattern,text)
    aadhaar_match = re.search(aadhaar_pattern,text)

    pan_score = 0
    aadhar_score = 0

    #Pattern
    if pan_match:
        pan_score += 50
    if aadhaar_match:
        aadhar_score += 50    
    #keyword score
    if "INCOME TAX" in text:
        pan_score += 20

    if "AADHAAR" in text or "UIDAI" in text:
        aadhar_score += 20

    #Final decision
    if pan_score > aadhar_score:
        return "PAN"
    elif aadhar_score > pan_score:
        return "AADHAAR"
    else:
        return "UNKNOWN"

