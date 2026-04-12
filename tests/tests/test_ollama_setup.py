#!/usr/bin/env python
"""
Test script to verify Ollama setup before running the full crew
"""
import requests
import sys
import os
from pathlib import Path

def test_ollama_connection():
    """Test if Ollama is running and accessible."""
    try:
        response = requests.get("http://localhost:11434/api/tags", timeout=5)
        if response.status_code == 200:
            models = response.json().get('models', [])
            print("✅ Ollama is running!")
            print(f"📋 Available models: {len(models)}")
            
            # Check if llama3.2 is available
            llama_models = [m for m in models if 'llama3.2' in m.get('name', '')]
            if llama_models:
                print("✅ Llama 3.2 model is available!")
                return True
            else:
                print("❌ Llama 3.2 model not found. Please run: ollama pull llama3.2")
                return False
        else:
            print(f"❌ Ollama responded with status {response.status_code}")
            return False
    except requests.exceptions.ConnectionError:
        print("❌ Cannot connect to Ollama. Make sure it's installed and running.")
        print("💡 Try running: ollama serve")
        return False
    except Exception as e:
        print(f"❌ Error testing Ollama: {e}")
        return False

def test_crew_with_ollama():
    """Test a simple crew execution with Ollama."""
    print("\n🧪 Testing CrewAI with Ollama...")
    
    # Add src to path
    sys.path.append('src')
    
    try:
        from telemedicine_project.crew import TelemedicineProject
        print("✅ CrewAI imports successful!")
        
        # Try to initialize the crew (this will test LLM connection)
        crew_instance = TelemedicineProject()
        print("✅ Crew initialization successful!")
        
        print("🎉 Everything looks good! Ready to run the full workflow.")
        return True
        
    except Exception as e:
        print(f"❌ Error with CrewAI setup: {e}")
        return False

def main():
    print("🔧 Testing Ollama Setup for CrewAI")
    print("=" * 50)
    
    # Test 1: Ollama connection
    ollama_ok = test_ollama_connection()
    
    if not ollama_ok:
        print("\n📋 Next Steps:")
        print("1. Install Ollama from https://ollama.ai/download")
        print("2. Run: ollama pull llama3.2")
        print("3. Run: ollama serve (if not auto-started)")
        print("4. Run this test again")
        return False
    
    # Test 2: CrewAI with Ollama
    crew_ok = test_crew_with_ollama()
    
    if crew_ok:
        print("\n🚀 Ready to Run!")
        print("Execute the full workflow with:")
        print("  cd src")
        print("  python -m telemedicine_project.main")
        return True
    else:
        print("\n⚠️ CrewAI setup needs attention")
        return False

if __name__ == "__main__":
    success = main()
    if not success:
        sys.exit(1)