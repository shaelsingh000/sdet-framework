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

### How do you integrate automation with CI/CD?

I designed the framework to run inside GitLab CI using a Python-based pipeline. 
Tests are triggered on every commit, executed in an isolated environment, and test results are published as pipeline artifacts.
This ensures regressions are detected early and bad code never reaches higher environments.


### Why do you run tests inside Docker?

Docker ensures test execution is consistent across local machines and CI.
It eliminates environment drift and makes the automation framework portable, scalable, and cloud-ready.
