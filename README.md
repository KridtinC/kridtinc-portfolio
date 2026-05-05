# Kridtin Chawalratikool — Portfolio

Personal portfolio website for **Kridtin Chawalratikool**, Senior Software Engineer at LINE MAN Wongnai.

> Built entirely with [Claude Code](https://claude.ai/code) by Anthropic.

**Live site:** https://kridtinc-portfolio.pages.dev

---

## Tech Stack

| Layer | Choice |
|---|---|
| Framework | [SvelteKit](https://kit.svelte.dev/) + TypeScript |
| Styling | [Tailwind CSS v4](https://tailwindcss.com/) |
| Charts | [Chart.js](https://www.chartjs.org/) |
| Deployment | [Cloudflare Pages](https://pages.cloudflare.com/) |
| Fonts | Inter + JetBrains Mono (Google Fonts, non-blocking) |

## Features

- **Hero** — Cursor-tracking glow effect, staggered entrance animation
- **About** — Bio and stats
- **Experience** — Tabbed timeline (LINE MAN Wongnai → LINE → KBTG → True Corp) + Volunteering section
- **Skills** — Three-tier: AI & Engineering / Experienced / Familiar
- **Work** — EK-style numbered project list with hover reveal and expandable interactive demos
  - **Prokedex Web** — Live Pokédex powered by [PokéAPI](https://pokeapi.co/)
  - **COVID-19 Dashboard** — Chart.js data visualization with country/metric toggles
- **Contact** — Email + social links
- **OG metadata** — Open Graph + Twitter Card for social sharing previews
- **Responsive** — Mobile hamburger menu, desktop fixed sidebar (Brittany Chiang layout)

## Project Structure

```
src/
├── app.css                     # Global styles, Tailwind v4 theme tokens
├── lib/
│   ├── data.ts                 # All site content (edit this to update info)
│   ├── stores.ts               # Active section store
│   └── components/
│       ├── Nav.svelte
│       ├── Hero.svelte
│       ├── About.svelte
│       ├── Experience.svelte
│       ├── Skills.svelte
│       ├── Work.svelte
│       ├── Contact.svelte
│       └── demos/
│           ├── ProkedexDemo.svelte
│           └── CovidDemo.svelte
├── routes/
│   ├── +layout.svelte          # Root layout, meta tags
│   └── +page.svelte            # Main page
static/
└── og-image.png                # Social preview image (1200×630)
scripts/
└── generate-og.mjs             # Regenerate og-image.png
```

## Getting Started

### Prerequisites

- Node.js v22+
- npm

### Install & Run

```bash
# Install dependencies
npm install

# Start development server
npm run dev
# → http://localhost:5173
```

### Build

```bash
npm run build
```

### Regenerate OG Image

```bash
node scripts/generate-og.mjs
```

## Updating Content

All site content lives in [`src/lib/data.ts`](src/lib/data.ts). Edit that file to update:

- `meta` — name, email, role, company, bio, about paragraphs
- `experience` — work history and bullet points
- `volunteering` — volunteer roles and links
- `skills` — AI tools, experienced, and familiar categories
- `projects` — work section items and demo types

## Deployment (Cloudflare Pages)

### First deploy

```bash
npm run build
npx wrangler pages deploy .svelte-kit/cloudflare --project-name kridtinc-portfolio --compatibility-flag nodejs_compat
```

### Subsequent deploys

```bash
npm run build && npx wrangler pages deploy .svelte-kit/cloudflare --project-name kridtinc-portfolio --compatibility-flag nodejs_compat
```

## Push to GitHub

```bash
# Add remote (first time only)
git remote add origin https://github.com/KridtinC/kridtinc-portfolio.git

# Push all commits
git push -u origin main

# Subsequent pushes
git add -A
git commit -m "your message"
git push
```

---

Built with [Claude Code](https://claude.ai/code) · Deployed on [Cloudflare Pages](https://pages.cloudflare.com/)
