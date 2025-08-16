// tests/404.spec.js
import { test, expect } from '@playwright/test';

test('404 page displays correctly', async ({ page }) => {
  await page.goto('/non-existent-page');

  // Expect the 404 heading to be visible
  await expect(page.getByText('404')).toBeVisible();

  // Expect the "Page Not Found" heading to be visible
  await expect(page.getByText('Page Not Found')).toBeVisible();

  // Expect the "Go back home" button to be visible
  await expect(page.getByRole('link', { name: 'Go back home' })).toBeVisible();
});

test('404 page navigation works', async ({ page }) => {
  await page.goto('/non-existent-page');

  // Click the "Go back home" button
  await page.click('text=Go back home');
  
  // Expect to be on the home page
  await expect(page).toHaveURL('/');
  await expect(page.getByText('Today\'s Exclusive')).toBeVisible();
});