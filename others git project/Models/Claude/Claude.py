import anthropic

client = anthropic.Anthropic(
    # defaults to os.environ.get("ANTHROPIC_API_KEY")
    api_key="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",
)
message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1371,
    temperature=0,
    system="WBS Layout: Code Exam Website with Grading Bot Integration \n1. Project Initiation\n1.1 Project Charter\nProject definition, goals, objectives\nStakeholder identification\nBudget and resource allocation\nHigh-level timeline\nRisks and assumptions\n1.2 Requirements Gathering\nDetailed functional and non-functional requirements\nBot integration specifications\nExam management features\n2. Planning\n2.1 Software Requirements Specification (SRS)\n2.2 Detailed Project Plan\nTask breakdown\nResource scheduling\nGantt Chart or similar timeline\n3. Design\n3.1 System Design\nHigh-level architecture\nDatabase design (if applicable)\nAPI specifications\n3.2 Website Design\nUI/UX mockups\nWireframes\nBranding and visual design\n4. Development\n4.1 Front-End Development\nHTML, CSS, JavaScript\nExam/quiz interface elements\nUser authentication and registration\n4.2 Backend Development\nServer-side logic (Python, Java, Node.js, etc.)\nDatabase implementation\nExam creation and management features\nGrading logic\n4.3 Bot Integration\nAPI interactions with ChatGPT 3.5 or Vertex\nTest case generation/handling\nFeedback mechanisms\n5. Testing\n5.1 Unit Testing\n5.2 Integration Testing\n5.3 System Testing\n5.4 User Acceptance Testing (UAT)\n6. Deployment\n6.1 CI/CD Setup\n6.2 Production Deployment\n6.3 Monitoring and Maintenance Planning\n7. Documentation\n7.1 System Documentation\n7.2 User Manual\n8. Project Closure\n8.1 Customer Feedback and Improvement\n8.2 Project Retrospective\n",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Give me feedback and Improve my WBS for my project. Then generate CPM (Critical Path Method) for each phrase of the project"
                }
            ]
        }
    ]
)
print(message.content)