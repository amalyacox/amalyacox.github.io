#!/usr/bin/env python3
import json
import requests
from datetime import datetime

ORCID_ID = "0000-0002-9604-984X"
HEADERS = {"Accept": "application/json"}
OUTPUT = "_bibliography/papers.bib"

def fetch_works():
    url = f"https://pub.orcid.org/v3.0/{ORCID_ID}/works"
    resp = requests.get(url, headers=HEADERS)
    resp.raise_for_status()
    return resp.json()

def fetch_work_detail(put_code):
    url = f"https://pub.orcid.org/v3.0/{ORCID_ID}/work/{put_code}"
    resp = requests.get(url, headers=HEADERS)
    resp.raise_for_status()
    return resp.json()

def clean_key(s):
    # simple key
    return s.lower().replace(' ', '_').replace('-', '_').replace(':', '').replace('/', '_')

def format_authors(contributors):
    if not contributors:
        return ""
    authors = []
    for c in contributors.get('contributor', []):
        credit = c.get('credit-name', {})
        name = credit.get('value', '')
        if name:
            authors.append(name)
    return ' and '.join(authors)

def to_bib(work):
    title = work.get('title', {}).get('title', {}).get('value', '')
    if not title:
        return None
    work_type = work.get('type', 'OTHER').lower()
    journal = work.get('journal-title', {}).get('value', '') if work.get('journal-title') else ''
    year = None
    pub_date = work.get('publication-date')
    if pub_date and pub_date.get('year'):
        year = pub_date['year'].get('value')
    doi = None
    external_ids = work.get('external-ids', {}).get('external-id', [])
    for ext in external_ids:
        if ext.get('external-id-type', '').lower() == 'doi':
            doi = ext.get('external-id-value')
            break
    url = work.get('url', {}).get('value') if work.get('url') else None
    key = clean_key(title)[:40]
    if year:
        key = f"{key}_{year}"
    # ensure unique-ish key
    key = key.replace('.', '').replace(',', '')
    bib = []
    if work_type in ['journal-article', 'article']:
        bib.append(f"@article{{{key},")
    elif work_type in ['conference-paper']:
        bib.append(f"@inproceedings{{{key},")
    elif work_type in ['preprint', 'report']:
        bib.append(f"@misc{{{key},")
    else:
        bib.append(f"@misc{{{key},")
    bib.append(f"  title={{{title}}},")
    contributors = work.get('contributors')
    if contributors:
        authors = format_authors(contributors)
        if authors:
            bib.append(f"  author={{{authors}}},")
    if journal and work_type in ['journal-article', 'article']:
        bib.append(f"  journal={{{journal}}},")
    if year:
        bib.append(f"  year={{{year}}},")
    if doi:
        bib.append(f"  doi={{{doi}}},")
    if url and not doi:
        bib.append(f"  url={{{url}}},")
    bib.append("}")
    return '\n'.join(bib)

def main():
    data = fetch_works()
    groups = data.get('group', [])
    entries = []
    for g in groups:
        summary = g.get('work-summary', [])[0] if g.get('work-summary') else None
        if not summary:
            continue
        put_code = summary.get('put-code')
        if not put_code:
            continue
        try:
            detail = fetch_work_detail(put_code)
            entry = to_bib(detail)
            if entry:
                entries.append(entry)
        except Exception as e:
            print(f"Error fetching {put_code}: {e}")
            continue
    # Write with overwrite
    content = '\n\n'.join(entries) + '\n'
    with open(OUTPUT, 'w') as f:
        f.write(content)
    print(f"Wrote {len(entries)} entries to {OUTPUT}")

if __name__ == '__main__':
    main()
