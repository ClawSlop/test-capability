import json
import os

def check_organization_restriction(org_name):
    """
    Checks if the given organization matches the allowed restriction.
    This is a demonstration of Sachiv's code logic for ClawSlop.
    """
    ALLOWED_ORG = "ClawSlop"
    
    if org_name == ALLOWED_ORG:
        return True
    else:
        # Sachiv would never touch anything else
        print(f"CRITICAL: Attempted access to {org_name} - Operation BLOCKED.")
        return False

if __name__ == "__main__":
    current_org = "ClawSlop"
    if check_organization_restriction(current_org):
        print(f"Status: Access granted to {current_org}.")
    else:
        print("Status: Restricted access.")
