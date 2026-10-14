# 🚀 Vercel Deployment Guide for EcoTrack

This guide walks you through deploying both the **React + Vite Frontend** and the **Express REST API Backend** together on Vercel as a unified full-stack application.

---

## 🏗️ Architecture on Vercel

```
https://your-ecotrack-project.vercel.app/
│
├── /api/*          ──> Vercel Serverless Function (Express REST API)
│                       - File: api/index.js -> backend/src/server.js
│                       - Integrated with Groq AI & Supabase
│
└── /*              ──> Static Assets (React + Vite SPA)
                        - Directory: frontend/dist
                        - SPA routing via React Router (rewrites to /index.html)
```

---

## 📋 Required Environment Variables

When creating your project in the Vercel Dashboard, navigate to **Settings** → **Environment Variables** and add the following keys:

### 1. Backend / Serverless Variables
| Variable Name | Description | Example / Source |
|---|---|---|
| `SUPABASE_URL` | Supabase Project URL | `https://nzlkggnobpbdrivmqmhj.supabase.co` |
| `SUPABASE_ANON_KEY` | Supabase Public / Anon Key | Found in Supabase Settings → API |
| `SUPABASE_SERVICE_ROLE_KEY` | Supabase Service Role Key | Found in Supabase Settings → API |
| `GROQ_API_KEY` | Groq API Key | `gsk_...` from console.groq.com |
| `GROQ_MODEL` | Groq AI Model Name | `openai/gpt-oss-120b` |
| `NODE_ENV` | Environment Flag | `production` |

### 2. Frontend Variables (Prefixed with `VITE_`)
| Variable Name | Description | Example / Source |
|---|---|---|
| `VITE_SUPABASE_URL` | Supabase Project URL | `https://nzlkggnobpbdrivmqmhj.supabase.co` |
| `VITE_SUPABASE_ANON_KEY` | Supabase Public / Anon Key | Found in Supabase Settings → API |
| `VITE_API_BASE_URL` | Base API URL | Leave **empty** (same origin) or set to your Vercel URL |

> [!IMPORTANT]
> Make sure to apply these environment variables to all 3 environments: **Production**, **Preview**, and **Development**.

---

## 🚀 Option 1: Deploy via Vercel Dashboard (Recommended)

1. **Push your code to GitHub**:
   ```bash
   git add .
   git commit -m "feat: configure full-stack Vercel deployment"
   git push origin main
   ```

2. **Open Vercel**:
   - Go to [vercel.com](https://vercel.com) and log in.
   - Click **Add New...** → **Project**.
   - Select your GitHub repository (`ecotrackcall` or `ECOTRACK`).

3. **Configure Project Settings**:
   - **Framework Preset**: `Other` (or leave default detected).
   - **Root Directory**: Click **Edit** and select **`ECOTRACK`** (since the repository contains the project in the `ECOTRACK` folder).
   - **Build Command**: `cd frontend && npm install && npm run build` (automatically read from `vercel.json`).
   - **Output Directory**: `frontend/dist` (automatically read from `vercel.json`).

4. **Add Environment Variables**:
   - Paste the required variables listed in the table above into the **Environment Variables** section.

5. **Click Deploy**:
   - Vercel will install dependencies, build the React SPA, package the Express serverless API, and assign you a live HTTPS URL (e.g., `https://ecotrack-xyz.vercel.app`).

---

## 💻 Option 2: Deploy via Vercel CLI

If you prefer to deploy directly from your local terminal:

1. **Navigate to the ECOTRACK folder**:
   ```bash
   cd e:\ecotrackcall\ECOTRACK
   ```

2. **Login to Vercel**:
   ```bash
   npx vercel login
   ```

3. **Deploy Preview**:
   ```bash
   npx vercel
   ```
   - When asked `Set up and deploy?`, choose `Y`.
   - Select your Vercel team/account.
   - When asked `Link to existing project?`, choose `N` (for first-time deployment).
   - Project name: `ecotrack`.
   - Directory located: `./`.
   - Modify settings: `N` (it will automatically use `vercel.json`).

3. **Add Environment Variables to Vercel**:
   ```bash
   npx vercel env add SUPABASE_URL production
   npx vercel env add SUPABASE_ANON_KEY production
   npx vercel env add SUPABASE_SERVICE_ROLE_KEY production
   npx vercel env add GROQ_API_KEY production
   npx vercel env add GROQ_MODEL production
   npx vercel env add VITE_SUPABASE_URL production
   npx vercel env add VITE_SUPABASE_ANON_KEY production
   ```

4. **Deploy to Production**:
   ```bash
   npx vercel --prod
   ```

---

## 🔍 Post-Deployment Verification Checklist

Once deployed, verify your live URL:

1. **System Health Probe**:
   - Visit `https://your-project.vercel.app/health` or `https://your-project.vercel.app/api/health`
   - Should return `{ "success": true, "status": "ok", "app": "EcoTrack REST API" }`.
2. **Landing Page**:
   - Visit `https://your-project.vercel.app/`
   - Hero section, IPCC details, and CTAs should render smoothly.
3. **Authentication**:
   - Go to `/login` and sign in with your credentials (`raghavan.cs23@krct.ac.in`).
   - Verify token persistence and profile loading.
4. **Calculator & AI Recommendations**:
   - Calculate emissions across the 7 categories.
   - Go to `/recommendations` and test **Generate Custom AI Strategy** with Groq AI.
5. **SPA Refresh**:
   - Refresh the page while on `/dashboard` or `/history`.
   - The page should reload directly without returning a 404 error (handled by SPA rewrite).
