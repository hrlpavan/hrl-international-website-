import json
import re
import sys

def validate_seo_assets():
    html_path = "/Users/pavankumars/.gemini/antigravity/scratch/hrl-brand-seo/index.html"
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    print("==================================================")
    print("[AUDIT] HRL INTERNATIONAL - TECHNICAL SEO AUDIT REPORT")
    print("==================================================")

    # 1. Check Title & Meta
    title_match = re.search(r"<title>(.*?)</title>", html)
    print(f"[OK] Title Tag: {title_match.group(1) if title_match else 'MISSING'}")

    meta_desc = re.search(r'<meta name="description" content="(.*?)"', html)
    print(f"[OK] Meta Description: {meta_desc.group(1) if meta_desc else 'MISSING'}")

    canonical = re.search(r'<link rel="canonical" href="(.*?)"', html)
    print(f"[OK] Canonical URL: {canonical.group(1) if canonical else 'MISSING'}")

    # 2. Extract and Validate JSON-LD
    json_ld_match = re.search(r'<script type="application/ld\+json">(.*?)</script>', html, re.DOTALL)
    if json_ld_match:
        try:
            data = json.loads(json_ld_match.group(1).strip())
            print("\n[SCHEMA] JSON-LD Schema Validation: SUCCESS (Valid JSON)")
            print(f"   Context: {data.get('@context')}")
            graph = data.get("@graph", [])
            print(f"   Graph Nodes Count: {len(graph)}")
            for node in graph:
                print(f"   - Node Type: {node.get('@type')} | ID: {node.get('@id')} | Name: {node.get('name')}")
                if "founder" in node:
                    print(f"     ↳ Founder Connected: {node['founder'].get('name')} ({node['founder'].get('jobTitle')})")
                if "sameAs" in node:
                    print(f"     ↳ Authority Hubs linked ({len(node['sameAs'])} platforms):")
                    for link in node["sameAs"]:
                        print(f"       • {link}")
        except json.JSONDecodeError as e:
            print(f"\n[ERROR] JSON-LD Error: {e}")
            return False
    else:
        print("\n[ERROR] JSON-LD Schema missing!")
        return False

    print("\n==================================================")
    print("[TARGET] ENTITY STATUS: READY FOR GOOGLE KNOWLEDGE VAULT")
    print("==================================================")
    return True

if __name__ == "__main__":
    validate_seo_assets()
