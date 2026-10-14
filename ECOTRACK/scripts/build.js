const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

const projectRoot = path.resolve(__dirname, '..');

console.log('[Build] Installing frontend dependencies...');
execSync('npm --prefix frontend install --include=dev', { cwd: projectRoot, stdio: 'inherit' });

console.log('[Build] Compiling frontend with Vite...');
execSync('npm --prefix frontend run build', { cwd: projectRoot, stdio: 'inherit' });

const srcDir = path.resolve(__dirname, '..', 'frontend', 'dist');
const destDir = path.resolve(__dirname, '..', 'dist');

console.log(`[Build] Copying assets from ${srcDir} to ${destDir}...`);
fs.cpSync(srcDir, destDir, { recursive: true });

if (fs.existsSync(path.join(destDir, 'index.html'))) {
  console.log('[Build] SUCCESS: dist/index.html is ready for Vercel deployment.');
} else {
  console.error('[Build] ERROR: dist/index.html was not found after copy.');
  process.exit(1);
}
