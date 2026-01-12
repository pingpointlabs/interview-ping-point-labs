"""
Setup verification script for PingPoint Labs interview exercise.
Run this to ensure all dependencies are properly installed.
"""

def verify_setup():
    """Verify that all required packages are installed."""
    required_packages = {
        'fitz': 'pymupdf',  # pymupdf imports as 'fitz'
        'pandas': 'pandas',
        'numpy': 'numpy',
    }

    missing_packages = []

    for import_name, package_name in required_packages.items():
        try:
            __import__(import_name)
            print(f"✅ {package_name} is installed")
        except ImportError:
            print(f"❌ {package_name} is NOT installed")
            missing_packages.append(package_name)

    if not missing_packages:
        print("\n✅ All dependencies installed successfully")
        return True
    else:
        print(f"\n❌ Missing packages: {', '.join(missing_packages)}")
        print("\nTo install missing packages, run:")
        print("  uv pip install .")
        return False


if __name__ == "__main__":
    verify_setup()
