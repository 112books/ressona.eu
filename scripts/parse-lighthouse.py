import json, os, sys

try:
    with open('/tmp/lh-report.json') as f:
        d = json.load(f)
    cats = d.get('categories', {})
    auds = d.get('audits', {})
    scores = {k: round(v.get('score', 0) * 100) for k, v in cats.items()}
    lcp = auds.get('largest-contentful-paint', {}).get('displayValue', 'n/a')
    fcp = auds.get('first-contentful-paint', {}).get('displayValue', 'n/a')
    cls = auds.get('cumulative-layout-shift', {}).get('displayValue', 'n/a')
    tbt = auds.get('total-blocking-time', {}).get('displayValue', 'n/a')

    summary = (
        "## Core Web Vitals — ressona.eu\n\n"
        "| Categoria | Puntuació |\n"
        "|-----------|----------|\n"
        "| Performance | {} |\n"
        "| Accessibility | {} |\n"
        "| Best Practices | {} |\n"
        "| SEO | {} |\n\n"
        "| Mètrica | Valor |\n"
        "|---------|-------|\n"
        "| LCP | {} |\n"
        "| FCP | {} |\n"
        "| CLS | {} |\n"
        "| TBT | {} |\n"
    ).format(
        scores.get('performance', '?'),
        scores.get('accessibility', '?'),
        scores.get('best-practices', '?'),
        scores.get('seo', '?'),
        lcp, fcp, cls, tbt
    )

    summary_path = os.environ.get('GITHUB_STEP_SUMMARY', '/tmp/summary.md')
    with open(summary_path, 'a') as f:
        f.write(summary)
    print(summary)
except Exception as e:
    print("Lighthouse report not available:", e)
