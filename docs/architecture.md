## Core Architecture

- ConfigReader handles environment-specific configuration
- BaseTest provides shared logging and fixtures
- APIClient abstracts HTTP interactions
- PyTest fixtures ensure session-level setup

This design enables scalability, CI/CD execution, and environment isolation.

## Flakiness Control

- WebDriver lifecycle managed via DriverFactory
- Parallel execution via pytest-xdist
- Automatic retries for transient failures
- Explicit waits in page objects
