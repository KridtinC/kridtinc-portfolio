/**
 * Generates /static/og-image.png from an inline SVG template.
 * Run: node scripts/generate-og.mjs
 * Requires: npm install -D sharp (one-time)
 */

import sharp from 'sharp';
import { writeFileSync } from 'fs';
import { fileURLToPath } from 'url';
import { dirname, join } from 'path';

const __dirname = dirname(fileURLToPath(import.meta.url));

const svg = `
<svg width="1200" height="630" viewBox="0 0 1200 630" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      @import url("https://fonts.googleapis.com/css2?family=Inter:wght@400;700&amp;display=swap");
    </style>
  </defs>

  <!-- Background -->
  <rect width="1200" height="630" fill="#0f0f0f"/>

  <!-- Subtle grid lines -->
  <line x1="0" y1="315" x2="1200" y2="315" stroke="#1a1a1a" stroke-width="1"/>
  <line x1="600" y1="0" x2="600" y2="630" stroke="#1a1a1a" stroke-width="1"/>

  <!-- Left accent bar -->
  <rect x="80" y="160" width="3" height="310" fill="#f97316" rx="2"/>

  <!-- Monospace label -->
  <text x="104" y="192" font-family="monospace" font-size="18" fill="#f97316" letter-spacing="4">SENIOR SOFTWARE ENGINEER</text>

  <!-- Name -->
  <text x="100" y="300" font-family="Arial, sans-serif" font-weight="700" font-size="80" fill="#f0f0f0">Kridtin</text>
  <text x="100" y="390" font-family="Arial, sans-serif" font-weight="700" font-size="80" fill="#f0f0f0">Chawalratikool</text>

  <!-- Tagline -->
  <text x="104" y="450" font-family="Arial, sans-serif" font-size="22" fill="#888888">Go · TypeScript · System Design · LINE MAN Wongnai</text>

  <!-- Bottom right: URL -->
  <text x="1100" y="580" font-family="monospace" font-size="16" fill="#444444" text-anchor="end">kridtinc-portfolio.pages.dev</text>

  <!-- Accent dot -->
  <circle cx="1120" y="580" r="4" fill="#f97316"/>
  <circle cx="1120" cy="576" r="4" fill="#f97316"/>
</svg>
`;

const outPath = join(__dirname, '../static/og-image.png');

sharp(Buffer.from(svg))
  .png()
  .toFile(outPath)
  .then(() => console.log(`✓ OG image written to static/og-image.png`))
  .catch((e) => console.error('Error:', e));
