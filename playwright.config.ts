import { defineConfig, devices } from '@playwright/test';
export default defineConfig({
  testDir: './tests', reporter: [['list'], ['html', { open: 'never' }]],
  webServer: { command: 'npm run preview -- --host 127.0.0.1 --port 4321 --foreground', port: 4321, reuseExistingServer: !process.env.CI },
  use: { baseURL: 'http://127.0.0.1:4321', screenshot: 'only-on-failure' },
  projects: [
    { name: 'desktop', use: { ...devices['Desktop Chrome'] } },
    { name: 'mobile', use: { ...devices['iPhone 13'], defaultBrowserType: 'chromium' } },
  ],
});
