# The Daily Drip

An automated service that generates one trending topic shirt per day using AI.

## Overview
This project automatically creates daily t-shirt designs based on trending topics and uploads them to a print-on-demand service. The goal is maximum simplicity with minimal maintenance while being deployable to a cheap cloud service for 24/7 operation.

## Key Features
- Daily AI-generated shirt designs based on trending topics
- Automatic upload to print-on-demand service
- Website for showcasing designs
- Scarcity model with one exclusive design per day
- Deployable to cost-effective cloud services

## Technology Stack
- **Backend**: Python, FastAPI
- **Frontend**: React.js, Tailwind CSS
- **Database**: PostgreSQL
- **AI**: Google Gemini
- **Deployment**: Google Cloud Run (backend), Vercel (frontend)
- **Print-on-Demand**: Printful API

## Project Structure
```
├── docs/                    # Project documentation
│   ├── prd.md              # Product Requirements Document
│   ├── front-end-spec.md   # UI/UX Specification
│   ├── fullstack-architecture.md  # System Architecture
│   ├── prd/shards/         # Sharded PRD documents
│   ├── stories/            # User stories
│   ├── tasks/              # Task tracking and project management
│   └── ...
├── src/                    # Source code (to be implemented)
│   ├── backend/            # Backend service
│   └── frontend/           # Frontend application
├── scripts/                # Utility scripts
├── .github/                # GitHub configurations
│   └── ISSUE_TEMPLATE/     # Issue templates for task tracking
├── README.md               # This file
└── ...
```

## Documentation
All project documentation is available in the `docs/` directory:
- [Project Brief](docs/project-brief.md)
- [Product Requirements Document](docs/prd.md)
- [Front-End Specification](docs/front-end-spec.md)
- [Full-Stack Architecture](docs/fullstack-architecture.md)
- [Project Summary](docs/project-summary.md)

## Task Tracking
We've established a comprehensive task tracking system with an MVP-focused approach:
- [Task Board](docs/tasks/task-board.md) - Overview of all tasks by user story (see also [MVP Task Board](docs/tasks/mvp-task-board.md))
- [Project Roadmap](docs/tasks/project-roadmap.md) - MVP-focused implementation timeline
- [Tracking Dashboard](docs/tasks/tracking-dashboard.md) - Real-time project status
- [Detailed Task Lists](docs/tasks/) - In-depth breakdown of tasks by user story

For our accelerated development approach, please see:
- [MVP Roadmap](docs/tasks/mvp-roadmap.md) - Streamlined 5-week implementation plan
- [MVP Task Board](docs/tasks/mvp-task-board.md) - Prioritized tasks for the minimal viable product
- [MVP Summary](docs/tasks/mvp-summary.md) - Overview of our MVP approach

## Development Status
This project is in the planning phase. The Greenfield Full-Stack workflow has been completed with all necessary artifacts created. Implementation can begin with the first user story: Trending Topic Analysis.

## Deployment
The system is designed to be deployed to cost-effective cloud services:
- Google Cloud Run for the backend service
- Vercel for the frontend application
- Supabase for the database
- Google Cloud Scheduler for daily execution

## Getting Started
1. Review the [MVP Roadmap](docs/tasks/mvp-roadmap.md) for our streamlined approach
2. Examine the [MVP Task Board](docs/tasks/mvp-task-board.md) for prioritized tasks
3. Set up the development environment
4. Begin implementation of the first user story

For context on our original plan, see:
- [Full Project Roadmap](docs/tasks/project-roadmap.md)
- [Full Task Board](docs/tasks/task-board.md)

## GitHub Issue Tracking
We use GitHub Issues for task tracking with the following templates:
- [User Story Implementation](.github/ISSUE_TEMPLATE/user-story.md)
- [Task](.github/ISSUE_TEMPLATE/task.md)
- [Bug Report](.github/ISSUE_TEMPLATE/bug-report.md)

## License
MIT