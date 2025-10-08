import builtins
import json as _json
from pathlib import Path

path = Path(__file__).parent / "data.json"
with open(path, "r") as file:
    data = _json.load(file)

print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':>6}  {'MTU':>6}")
print("-" * 50, "-" * 20, " ", "-" * 6, " ", "-" * 6)

for item in data["imdata"]:
    attrs = item["l1PhysIf"]["attributes"]
    print(f"{attrs['dn']:<50} {attrs.get('descr', ''):<20} {attrs['speed']:>6}  {attrs['mtu']:>6}")