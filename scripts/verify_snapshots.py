"""Verify all manifest-listed workshop snapshots without using a network."""
import hashlib,json
from pathlib import Path

def verify(root):
    data=Path(root)/'data/sample_or_fallback'
    manifest=json.loads((data/'manifest.json').read_text(encoding='utf-8'))
    for item in manifest['sources']:
        path=(data/item['file']).resolve()
        if not path.is_relative_to(data.resolve()):raise ValueError('Manifest path escapes snapshot directory.')
        if not path.is_file():raise ValueError(f'Missing snapshot: {item["file"]}')
        if hashlib.sha256(path.read_bytes()).hexdigest()!=item['sha256']:raise ValueError(f'Checksum mismatch: {item["file"]}')
    return len(manifest['sources'])

if __name__=='__main__':
    print(f'PASS: {verify(Path(__file__).resolve().parents[1])} snapshot checksums verified offline.')
