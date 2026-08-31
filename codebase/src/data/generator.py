"""Synthetic bug reports labeled by severity."""

from __future__ import annotations
import random
from typing import Dict, List
import numpy as np
import pandas as pd

SEVERITY_TEMPLATES: Dict[str, List[Dict[str, str]]] = {
    "Critical": [
        {"title": "Production database completely down", "description": "Primary DB unreachable. All customer transactions failing. Immediate revenue impact."},
        {"title": "Security breach - customer data exposed", "description": "Unauthorized access to user PII detected. Potential data leak. Legal and compliance risk."},
        {"title": "Payment gateway offline for all regions", "description": "No payments can be processed. Complete checkout outage across all markets."},
        {"title": "Auth service down - users cannot log in", "description": "Login and SSO completely broken. Entire user base locked out."},
        {"title": "Ransomware detected on production servers", "description": "Malware encrypting files on prod cluster. Emergency incident response required."},
    ],
    "High": [
        {"title": "Checkout fails for 30% of users", "description": "Intermittent payment errors. Significant conversion drop. Affects major markets."},
        {"title": "API latency spiked above SLA", "description": "P99 latency >5s on core APIs. Customer complaints increasing."},
        {"title": "Mobile app crashes on startup for Android 14", "description": "Large segment of Android users cannot open the app after latest OS update."},
        {"title": "Email delivery delayed by several hours", "description": "Transactional emails (orders, password reset) delayed. Support load rising."},
        {"title": "Search returns incorrect ranking", "description": "Product search relevance broken after index rebuild. Sales impact likely."},
    ],
    "Medium": [
        {"title": "Export CSV fails for large reports", "description": "Reports with more than 10k rows fail to export. Workaround: split queries."},
        {"title": "Dark mode contrast issues on settings page", "description": "Some labels hard to read in dark theme. Cosmetic but affects usability."},
        {"title": "Notification badge count incorrect", "description": "Unread count sometimes shows stale number until refresh."},
        {"title": "Slow loading of analytics dashboard", "description": "Dashboard takes 8-10 seconds to load. Acceptable but suboptimal."},
        {"title": "Typo in error message on form validation", "description": "Misspelled word in validation toast. Low user impact."},
    ],
    "Low": [
        {"title": "Footer copyright year outdated", "description": "Footer still shows previous year. Purely cosmetic."},
        {"title": "Minor spacing inconsistency on buttons", "description": "Primary button padding slightly uneven on one page."},
        {"title": "Console warning on page load", "description": "Harmless React key warning in browser console. No functional impact."},
        {"title": "Tooltip text could be clearer", "description": "Help tooltip wording is ambiguous. Suggestion for copy improvement."},
        {"title": "Missing alt text on decorative icon", "description": "Accessibility nit: decorative image should have empty alt."},
    ],
}


def generate_bug_dataset(n_samples: int = 4000, seed: int = 42) -> pd.DataFrame:
    random.seed(seed)
    np.random.seed(seed)
    severities = list(SEVERITY_TEMPLATES.keys())
    records = []
    for i in range(n_samples):
        sev = random.choice(severities)
        tmpl = random.choice(SEVERITY_TEMPLATES[sev])
        title = tmpl["title"]
        desc = tmpl["description"]
        if random.random() < 0.25:
            desc = desc + f" Reported by user-{random.randint(1000,9999)}."
        if random.random() < 0.15:
            title = title + f" [env:{random.choice(['prod','staging','qa'])}]"
        full = f"Title: {title}\nDescription: {desc}"
        records.append({
            "bug_id": f"BUG-{i+1:05d}",
            "title": title,
            "description": desc,
            "full_text": full,
            "severity": sev,
        })
    return pd.DataFrame(records)


if __name__ == "__main__":
    df = generate_bug_dataset(200)
    print(df["severity"].value_counts())
    print(df.head(2))
