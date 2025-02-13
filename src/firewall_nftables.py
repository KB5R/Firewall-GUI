#!/usr/bin/env python3

import nftables
import json

nft = nftables.Nftables()
nft.set_json_output(True)
rc, output, error = nft.cmd("list ruleset")
print(json.loads(output))
