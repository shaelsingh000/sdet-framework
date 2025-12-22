## Core Architecture

- ConfigReader handles environment-specific configuration
- BaseTest provides shared logging and fixtures
- APIClient abstracts HTTP interactions
- PyTest fixtures ensure session-level setup

This design enables scalability, CI/CD execution, and environment isolation.
