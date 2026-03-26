import json
import os

def check_organization_restriction(org_name):
    """
    Checks if the given organization matches the allowed restriction.
    This is a demonstration of Sachiv's code logic for ClawSlop.
    """
    ALLOWED_ORG = "ClawSlop"
    
    # Strictly enforced by Sachiv the Assistant
    if org_name == ALLOWED_ORG:
        print(f"PERMISSION GRANTED: Working on {org_name}...")
        return True
    else:
        # Sachiv would never touch anything else
        print(f"CRITICAL ERROR: Attempted access to {org_name} - Access Denied by Sachiv.")
        return False

if __name__ == "__main__":
    current_org = "ClawSlop"
    if check_organization_restriction(current_org):
        print(f"Status: Access granted to {current_org}.")
    else:
        print("Status: Restricted access.")
