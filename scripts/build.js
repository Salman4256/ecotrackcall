const { execSync } = require('child_process');
const fs = require('fs');
const path = require('path');

console.log('[Build Root] Running ECOTRACK build...');
execSync('node ECOTRACK/scripts/build.js', { stdio: 'inherit' });

const srcDir = path.resolve(__dirname, '..', 'ECOTRACK', 'dist');
const destDir = path.resolve(__dirname, '..', 'dist');

console.log(`[Build Root] Copying assets to root dist: ${destDir}...`);
fs.cpSync(srcDir, destDir, { recursive: true });

if (fs.existsSync(path.join(destDir, 'index.html'))) {
  console.log('[Build Root] SUCCESS: root dist/index.html is ready for Vercel deployment.');
} else {
  console.error('[Build Root] ERROR: root dist/index.html was not found after copy.');
  process.exit(1);
}
