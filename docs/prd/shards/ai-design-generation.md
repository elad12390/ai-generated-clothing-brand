# Shard 2: AI Design Generation

## User Story
As a system, I want to generate ONE exclusive shirt design per day so that scarcity is maintained

## Description
The system needs to integrate with Gemini AI to generate ONE exclusive shirt design per day based on the selected trending topic, including topic text, AI-generated central image, and QR code.

## Acceptance Criteria
- System generates ONE shirt design per day using Gemini AI
- Design includes topic text prominently displayed at top
- Design includes AI-generated central image
- Design includes QR code on back linking to product page
- System handles AI service failures gracefully
- System stays within free-tier usage limits

## Technical Requirements
- Integration with Google Gemini AI service
- Text overlay functionality for topic display
- QR code generation functionality
- Image composition capabilities
- Rate limiting to stay within free-tier quotas
- Error handling for AI service failures

## Dependencies
- Google Gemini AI service
- Image processing libraries
- QR code generation library