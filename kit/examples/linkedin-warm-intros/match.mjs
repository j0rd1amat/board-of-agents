#!/usr/bin/env node
// Finds your own LinkedIn connections who work at the companies you care about.
// It reads two files on your computer and writes a third. It sends nothing and opens no website.
//
//   node match.mjs <Connections.csv> <companies.csv>            match and print the summary
//   node match.mjs <Connections.csv> <companies.csv> --min-fit 6   only companies scored 6 or more
//
// Connections.csv: from LinkedIn's data archive (Settings → Data privacy → Download my data → larger data archive).
// companies.csv:   your list. One column "company" is enough. Optional columns: "fit" (a score, 0 to 10) and
//                  "status" (anything you want carried over, such as "already talking").
// never.txt:       optional, next to this script. One company per line that must never be listed
//                  (your employer, a client you may not approach).
// Output: matches.csv next to this script, sorted with the people most worth writing to first.

import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const HERE = path.dirname(fileURLToPath(import.meta.url));
const OUT = path.join(HERE, 'matches.csv');

// Who counts as "the buyer" depends on what you sell. Change this line to your buyer's job titles.
const BUYER = /\b(people|human resources|hr|talent|benefits|workplace|employee experience)\b/i;
const SENIOR = /\b(chief|ceo|coo|cfo|cto|cmo|founder|co-founder|president|vp|vice president|director|head|partner|general manager|managing director)\b/i;

function parse(text) {
  const rows = []; let row = []; let cur = ''; let q = false;
  for (let i = 0; i < text.length; i++) {
    const c = text[i];
    if (q) { if (c === '"' && text[i + 1] === '"') { cur += '"'; i++; } else if (c === '"') q = false; else cur += c; }
    else if (c === '"') q = true;
    else if (c === ',') { row.push(cur); cur = ''; }
    else if (c === '\n') { row.push(cur); rows.push(row); row = []; cur = ''; }
    else if (c !== '\r') cur += c;
  }
  if (cur !== '' || row.length) { row.push(cur); rows.push(row); }
  return rows;
}
const esc = (v) => { v = String(v ?? '').replace(/\s+/g, ' ').trim(); return /[",]/.test(v) ? `"${v.replace(/"/g, '""')}"` : v; };
function load(file, headerHas) {
  const rows = parse(fs.readFileSync(file, 'utf8').replace(/^﻿/, '')).filter((r) => r.some((x) => x !== ''));
  // LinkedIn puts a few "Notes:" lines above the real header
  const h = rows.findIndex((r) => r.some((x) => x.trim().toLowerCase() === headerHas));
  if (h < 0) { console.error(`${file}: no column called "${headerHas}"`); process.exit(2); }
  const head = rows[h].map((x) => x.trim());
  return rows.slice(h + 1).map((r) => Object.fromEntries(head.map((k, i) => [k, r[i] ?? ''])));
}
// "Acme Inc." and "ACME" are the same company; "Beta (formerly Alpha)" answers to both names
const SUFFIX = /(inc|llc|ltd|limited|gmbh|sl|sa|sas|bv|ab|plc|corp|corporation|group|labs|technologies|technology|holdings|company|co)$/;
const key = (s) => { let k = (s || '').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g, '').replace(/[^a-z0-9]/g, ''); for (let i = 0; i < 2; i++) k = k.replace(SUFFIX, ''); return k; };
const keys = (name) => { const out = new Set(); const inner = /\((.*?)\)/.exec(name || ''); if (inner) out.add(key(inner[1].replace(/^formerly\s+/i, ''))); out.add(key((name || '').replace(/\(.*?\)/g, ''))); out.delete(''); return [...out]; };

const [connFile, coFile] = process.argv.slice(2);
const mi = process.argv.indexOf('--min-fit');
const minFit = mi > 0 ? Number(process.argv[mi + 1]) : 0;
if (!connFile || !coFile || !fs.existsSync(connFile) || !fs.existsSync(coFile)) { console.error('Usage: node match.mjs <Connections.csv> <companies.csv> [--min-fit N]'); process.exit(2); }

const neverFile = path.join(HERE, 'never.txt');
const NEVER = fs.existsSync(neverFile) ? fs.readFileSync(neverFile, 'utf8').split('\n').map((l) => key(l.replace(/#.*/, ''))).filter((k) => k.length >= 3) : [];

const companies = load(coFile, 'company');
const byKey = new Map();
// names shorter than 3 letters match too many things: they are skipped and reported
const tooShort = [];
for (const a of companies) for (const k of keys(a.company)) { if (k.length < 3) tooShort.push(a.company); else if (!byKey.has(k)) byKey.set(k, a); }

const conns = load(connFile, 'first name');
const rows = []; let never = 0;
for (const c of conns) {
  const co = c.Company || ''; if (!co) continue;
  const ks = keys(co);
  if (ks.some((k) => NEVER.some((n) => k.startsWith(n)))) { never++; continue; }
  const a = ks.map((k) => byKey.get(k)).find(Boolean);
  if (!a) continue;
  const fit = a.fit === undefined || a.fit === '' ? '' : Number(a.fit) || 0;
  if (fit !== '' && fit < minFit) continue;
  const title = c.Position || '';
  const role = BUYER.test(title) ? 'buyer' : SENIOR.test(title) ? 'senior' : 'employee';
  rows.push({ first_name: c['First Name'], last_name: c['Last Name'], title, company: co, your_company: a.company, fit, role, status: a.status || '', connected_on: c['Connected On'], url: c.URL });
}
const order = { buyer: 0, senior: 1, employee: 2 };
rows.sort((x, y) => order[x.role] - order[y.role] || (Number(y.fit) || 0) - (Number(x.fit) || 0) || x.your_company.localeCompare(y.your_company));
const COLS = ['first_name', 'last_name', 'title', 'company', 'your_company', 'fit', 'role', 'status', 'connected_on', 'url'];
fs.writeFileSync(OUT, [COLS.join(','), ...rows.map((r) => COLS.map((k) => esc(r[k])).join(','))].join('\n') + '\n');

const n = (f) => rows.filter(f).length;
const cos = new Set(rows.map((r) => r.your_company));
console.log(`${conns.length} connections read · ${rows.length} work at ${cos.size} of your ${companies.length} companies (${never} at never-contact companies left out)`);
console.log(`by role: buyer ${n((r) => r.role === 'buyer')} · senior ${n((r) => r.role === 'senior')} · other employees ${n((r) => r.role === 'employee')}`);
if (tooShort.length) console.log(`not matched, name too short to match safely: ${tooShort.join(', ')}`);
console.log(`written: ${OUT}`);
