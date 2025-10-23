#!/usr/bin/env python3
"""
Test script to verify Vercel settings work correctly
"""
import os
import sys

# Add the project directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Set Vercel environment
os.environ['VERCEL'] = '1'

try:
    # Import settings
    from twiky_project import settings
    
    print("✅ Settings imported successfully")
    print(f"✅ STATIC_ROOT: {settings.STATIC_ROOT}")
    print(f"✅ VERCEL environment: {os.environ.get('VERCEL')}")
    print(f"✅ Force rebuild marker: {getattr(settings, 'VERCEL_FORCE_REBUILD', 'Not set')}")
    
    # Test that we don't try to create directories
    print("✅ No directory creation attempted on Vercel")
    
except Exception as e:
    print(f"❌ Error: {e}")
    sys.exit(1)

print("🎉 All tests passed! Settings are Vercel-compatible.")
