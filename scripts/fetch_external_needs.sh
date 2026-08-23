#!/usr/bin/env bash
# scripts/fetch_external_needs.sh
#
# Export this repo's own root-project needs (org_req, risk, problem, change,
# exception, tool, infra) and place the result where needs/conf.py's
# needs_external_needs expects it: needs/_external_needs/org_needs.json.
# This is the exact mechanism the real "Export organisation/governance/
# needs.json" step of .github/workflows/ci-needs.yml already runs inline —
# pulled out here as a standalone, reusable script instead of living only
# as YAML, so it can be run locally too.
#
# organisation/ (org_req's home) is no longer part of this repo — it's
# owned by qorix-gnc and only ever materialized locally by
# scripts/sync_org_content.sh (gitignored, never committed here; see
# scripts/README.md). This script used to assume organisation/ was always
# present because it was committed; now it checks for it explicitly and
# fails fast with a clear message instead of silently exporting zero
# org_req needs, which would make every `:links: ORG_*` citation in
# needs/ resolve as broken with no obvious cause.
#
# Requires the root project's own doc-build dependencies (see
# .github/workflows/ci-needs.yml's "Install root-project deps" step):
#   pip install sphinx sphinx-needs sphinxcontrib-plantuml Pillow
#   apt-get install -y default-jre-headless graphviz plantuml
# Not installed by this script — it assumes the environment already has
# them (matching how ci-needs.yml itself separates the two steps).
#
# Usage: scripts/fetch_external_needs.sh

set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST_DIR="${REPO_ROOT}/needs/_external_needs"
DEST_FILE="${DEST_DIR}/org_needs.json"
BUILD_DIR="${REPO_ROOT}/_build/org_needs"

cd "${REPO_ROOT}"

if [[ ! -d "${REPO_ROOT}/organisation/governance" ]]; then
  echo "error: organisation/governance/ not found — org_req needs live there and it's not present." >&2
  echo "       organisation/ is no longer committed to this repo (owned by qorix-gnc now)." >&2
  echo "       Run scripts/sync_org_content.sh first, then re-run this script." >&2
  exit 1
fi

echo "-- building root project's needs export (org_req, risk, problem, change, exception, tool, infra)"
sphinx-build -b needs . "${BUILD_DIR}"

if [[ ! -f "${BUILD_DIR}/needs.json" ]]; then
  echo "error: expected ${BUILD_DIR}/needs.json was not produced" >&2
  exit 1
fi

mkdir -p "${DEST_DIR}"
cp "${BUILD_DIR}/needs.json" "${DEST_FILE}"

echo "-- wrote ${DEST_FILE}"
echo "   needs/_external_needs/ is CI-generated, never committed — matches"
echo "   needs/conf.py's own comment on needs_external_needs. Re-run this"
echo "   any time root-project needs change before building needs/."
