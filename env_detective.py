#!/usr/bin/env python3
"""
.env Detective - Because your environment variables are playing hide and seek
"""

import os
import sys
import re
from pathlib import Path

def investigate_env_file(filepath='.env'):
    """CSI: Config Scene Investigation - finds clues in your .env crime scene"""
    path = Path(filepath)
    
    if not path.exists():
        print(f"🔍 Case File Missing: '{filepath}' not found. Did you check the evidence locker?")
        return False
    
    print(f"🔍 Examining evidence file: {path.absolute()}")
    print("-" * 50)
    
    issues = []
    line_num = 0
    
    with open(path, 'r') as f:
        for line in f:
            line_num += 1
            line = line.rstrip('\n')
            
            # Skip empty lines and comments
            if not line.strip() or line.strip().startswith('#'):
                continue
            
            # Check for common issues
            if '=' not in line:
                issues.append(f"Line {line_num}: No '=' found - variables need assignments, not suggestions")
                continue
            
            key, value = line.split('=', 1)
            key = key.strip()
            
            # Check key naming
            if not re.match(r'^[A-Za-z_][A-Za-z0-9_]*$', key):
                issues.append(f"Line {line_num}: Invalid variable name '{key}' - Python will judge you")
            
            # Check if loaded in environment
            if key in os.environ:
                print(f"✅ Line {line_num}: '{key}' successfully infiltrated the environment")
            else:
                issues.append(f"Line {line_num}: '{key}' failed to load - check your dotenv library's mood")
    
    print("-" * 50)
    
    if issues:
        print("🚨 SUSPICIOUS ACTIVITY DETECTED:")
        for issue in issues:
            print(f"  • {issue}")
        print(f"\n🔧 Total issues: {len(issues)}")
        return False
    else:
        print("🎉 Case closed! All variables appear to be behaving properly.")
        print("(But remember, environment variables are sneaky little things)")
        return True

if __name__ == '__main__':
    file_to_check = sys.argv[1] if len(sys.argv) > 1 else '.env'
    success = investigate_env_file(file_to_check)
    sys.exit(0 if success else 1)
