import pytest
from playwright.sync_api import Page
from axe_playwright_python.sync_playwright import Axe
from pages.login_page import LoginPage


@pytest.mark.a11y
def test_wcag_accessibility_scan(page: Page):
    """Runs automated WCAG 2.1 accessibility checks using Axe-core."""
    login_page = LoginPage(page)
    login_page.navigate()

    axe = Axe()
    results = axe.run(page)

    violations = results.response.get("violations", [])
    critical_or_serious = [
        v for v in violations if v.get("impact") in ("critical", "serious")
    ]

    assert len(critical_or_serious) == 0, (
        f"Found {len(critical_or_serious)} critical/serious WCAG violations: "
        f"{[v['id'] for v in critical_or_serious]}"
    )
