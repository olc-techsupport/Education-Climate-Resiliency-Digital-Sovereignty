"""Execute the three tracks with outbound socket connections blocked in each kernel."""
from pathlib import Path
import json,sys
import nbformat
from nbclient import NotebookClient
from verify_snapshots import verify

ROOT=Path(__file__).resolve().parents[1]
print('Verified snapshots:',verify(ROOT))
OUTPUT=ROOT/'outputs/validation'
OUTPUT.mkdir(parents=True,exist_ok=True)
guard=nbformat.v4.new_code_cell('''import socket
_original_connect = socket.socket.connect
def _offline_connect(self, address):
    if isinstance(address, tuple) and address[0] not in ("127.0.0.1", "::1", "localhost"):
        raise RuntimeError("Outbound network disabled for workshop validation")
    return _original_connect(self, address)
socket.socket.connect = _offline_connect
''')
for name in ['01_guided_explorer.ipynb','02_data_investigator.ipynb','03_technical_extender.ipynb']:
    nb=nbformat.read(ROOT/'tracks'/name,as_version=4)
    nb.cells.insert(0,guard)
    NotebookClient(nb,timeout=120,kernel_name='python3',resources={'metadata':{'path':str(ROOT)}}).execute()
    nbformat.write(nb,OUTPUT/name)
    print('PASS offline:',name)
print('Executed copies saved to outputs/validation; learner notebooks unchanged.')
