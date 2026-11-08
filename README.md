# Noor Mkdad

I'm a platform and systems engineer. I build Linux infrastructure and LLM
serving systems, and I publish the benchmarks behind them.

[noorhayatywadam@gmail.com](mailto:noorhayatywadam@gmail.com) ·
[resume](https://drmkdaddy.github.io/DrMkdaddy/resume.pdf) ·
[stanzaapi.com](https://stanzaapi.com) ·
[engineering notes](https://github.com/StanzaAPI/engineering-notes)

## Selected work

**[Stanza API](https://stanzaapi.com)**: a commercial API platform I built and
run. It has 12 APIs for healthcare claims, payments, and supply chain data,
with SDKs in four languages and an MCP server so agents can call them.

**[X12 parser](https://github.com/StanzaAPI/benchmark-harness)**: a streaming
parser for healthcare claims. It reads 255,000 records in 14.2 seconds inside a
25 MB memory cap. Under the same cap, node-x12 takes 49% longer and x12-parser
2.7x; with no cap, node-x12 matches it. The benchmark harness is public.

**[KV cache](https://github.com/DrMkdaddy/valkey-kv-l2)**: a tiered KV cache
for LLM serving. A fixed pool served 4 of 200 sequences; spilling to Valkey
served all 200. Restoring a prefix only beats recomputing it above about 4k
tokens, which I measured against prefill.

**[Scheduler](https://github.com/DrMkdaddy/kv-serving-scheduler)**: a request
scheduler for llama.cpp. It decides which requests run and cancels some when
the KV budget runs out. I measured it at 120% of capacity and recorded how long
the slowest requests waited and how many finished on time, including the
policies that drop load.

**[Local inference stack](https://github.com/DrMkdaddy/local-inference-stack)**:
an OpenAI-compatible gateway for one RX 9070 XT. It sends each request to the
cheapest model that fits and refuses one that would exceed a cost ceiling. It
runs at $0.19–0.41 per million tokens.

**[llama.cpp patch](https://github.com/DrMkdaddy/llama-vulkan-matvec-rdna4)**:
a Vulkan kernel patch that stops llama.cpp from unpacking the same weights for
every request in a batch. 13.4% faster overall across 8 slots, identical output,
and no change for a single request. Upstream PR
[#31022](https://github.com/ggml-org/llama.cpp/pull/31022).

## Background

My home lab runs Proxmox, provisioned with OpenTofu and configured with NixOS.
I also run LLMs on one RX 9070 XT. Day to day I write Go, TypeScript, and
Python.

I'm looking for a full-time platform, backend, or systems role.
