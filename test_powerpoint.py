#!/usr/bin/env python
"""
Test script to verify PowerPoint generation works independently
"""
import os
import sys
sys.path.append('src')

from telemedicine_project.tools.powerpoint_tool import PowerPointGeneratorTool

def test_powerpoint_generation():
    """Test PowerPoint generation with sample markdown content."""
    
    # Sample markdown content
    sample_markdown = """
# The Future of Telemedicine: AI-Driven Diagnostics

## Executive Summary
Telemedicine is revolutionizing healthcare delivery through AI-powered diagnostic tools.
- Market growth projected at 25% CAGR through 2028
- AI accuracy rates exceeding 95% in specific diagnostic areas
- Regulatory frameworks evolving to support innovation

## Market Trends and Growth
The telemedicine market is experiencing unprecedented expansion.
- Global market size reached $83.5 billion in 2022
- Expected to reach $396.8 billion by 2027
- COVID-19 accelerated adoption by 5-7 years

### Key Market Drivers
- Aging population demographics
- Healthcare accessibility challenges
- Cost reduction pressures
- Technology advancement

## Technical Challenges and Solutions
AI integration faces several technical hurdles.
- Data interoperability issues
- Algorithm bias and fairness
- Real-time processing requirements
- Privacy and security concerns

### Emerging Solutions
- Federated learning approaches
- Edge computing deployment
- Blockchain for data integrity
- Advanced encryption methods

## Clinical Impact and Outcomes
AI-driven diagnostics show promising clinical results.
- Reduced diagnostic errors by 40%
- Faster time to treatment decisions
- Improved patient satisfaction scores
- Enhanced physician productivity

### Success Stories
- Radiology AI detecting early-stage cancers
- Dermatology apps for skin condition screening
- Cardiology monitoring through wearables
- Mental health assessment tools

## Future Outlook and Recommendations
The future holds immense potential for telemedicine advancement.
- Integration with IoT devices
- Personalized medicine approaches
- Global healthcare democratization
- Regulatory harmonization needs
"""

    # Check if slide master exists
    slide_master_path = "AI Bubble_ Detection, Prevention, and Investment Strategies (1).pptx"
    if not os.path.exists(slide_master_path):
        print(f"❌ Slide Master file not found: {slide_master_path}")
        return False
    
    print("🔧 Testing PowerPoint Generation Tool...")
    print(f"📁 Slide Master: {slide_master_path}")
    print("📝 Sample Content: Telemedicine research markdown")
    print("-" * 60)
    
    # Create tool instance
    tool = PowerPointGeneratorTool()
    
    # Test the tool
    result = tool._run(
        markdown_content=sample_markdown,
        slide_master_path=slide_master_path,
        output_filename="Test_Presentation.pptx",
        min_slides=10,
        max_slides=15
    )
    
    print(result)
    
    # Check if output file was created
    if os.path.exists("Test_Presentation.pptx"):
        print("\n✅ SUCCESS: Test_Presentation.pptx created successfully!")
        return True
    else:
        print("\n❌ FAILED: PowerPoint file was not created")
        return False

if __name__ == "__main__":
    success = test_powerpoint_generation()
    if success:
        print("\n🎉 PowerPoint tool is working correctly!")
        print("📋 Next step: Configure API keys and run the full crew")
    else:
        print("\n⚠️  PowerPoint tool needs troubleshooting")
        print("💡 Check python-pptx installation and slide master file")