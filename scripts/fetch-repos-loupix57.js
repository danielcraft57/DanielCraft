#!/usr/bin/env node
/**
 * Script Node pour recuperer les repos GitHub de loupix57 et generer
 * un JSON simplifie utilise par la modale "Voir les details" du portfolio.
 * Usage: node scripts/fetch-repos-loupix57.js
 * Sortie: assets/data/repos-loupix57.json
 */

const fs = require('fs');
const path = require('path');

const API_URL = 'https://api.github.com/users/loupix57/repos?per_page=100&sort=updated';
const OUTPUT_PATH = path.join(__dirname, '..', 'assets', 'data', 'repos-loupix57.json');

function simplify(repo) {
  return {
    name: repo.name,
    full_name: repo.full_name,
    description: repo.description || '',
    html_url: repo.html_url,
    clone_url: repo.clone_url,
    language: repo.language || null,
    languages_url: repo.languages_url,
    stargazers_count: repo.stargazers_count,
    forks_count: repo.forks_count,
    open_issues_count: repo.open_issues_count,
    size: repo.size,
    default_branch: repo.default_branch,
    created_at: repo.created_at,
    updated_at: repo.updated_at,
    pushed_at: repo.pushed_at,
    homepage: repo.homepage,
    topics: repo.topics || [],
    license: repo.license ? repo.license.spdx_id || repo.license.key : null,
    archived: repo.archived,
    fork: repo.fork,
    has_wiki: repo.has_wiki,
    has_pages: repo.has_pages
  };
}

async function main() {
  const dataDir = path.dirname(OUTPUT_PATH);
  if (!fs.existsSync(dataDir)) {
    fs.mkdirSync(dataDir, { recursive: true });
  }

  let allRepos = [];
  let url = API_URL;

  while (url) {
    const res = await fetch(url, {
      headers: { 'User-Agent': 'DanielCraft-fetch-repos/1.0' }
    });
    if (!res.ok) {
      throw new Error(`GitHub API: ${res.status} ${res.statusText}`);
    }
    const page = await res.json();
    allRepos = allRepos.concat(page);

    const link = res.headers.get('Link');
    const nextMatch = link && link.match(/<([^>]+)>;\s*rel="next"/);
    url = nextMatch ? nextMatch[1] : null;
  }

  const simplified = allRepos.map(simplify);
  fs.writeFileSync(OUTPUT_PATH, JSON.stringify(simplified, null, 2), 'utf8');
  console.log(`[OK] ${simplified.length} repos ecrits dans ${OUTPUT_PATH}`);
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
